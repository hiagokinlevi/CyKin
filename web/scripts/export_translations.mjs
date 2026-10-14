// Read the existing browser translation dictionary without duplicating it.
import fs from 'node:fs';
import ts from 'typescript';

const source = ts.createSourceFile('i18n.ts', fs.readFileSync('src/lib/i18n.ts', 'utf8'), ts.ScriptTarget.Latest, true);
let dictionary;
for (const statement of source.statements) {
  if (!ts.isVariableStatement(statement)) continue;
  for (const declaration of statement.declarationList.declarations) {
    if (declaration.name.getText(source) !== 'copy' || !ts.isObjectLiteralExpression(declaration.initializer)) continue;
    dictionary = {};
    for (const property of declaration.initializer.properties) {
      if (!ts.isPropertyAssignment(property) || !ts.isArrayLiteralExpression(property.initializer)) continue;
      const key = property.name.text;
      const values = property.initializer.elements.map(value => value.text);
      if (typeof key === 'string' && values.length === 2 && values.every(value => typeof value === 'string')) dictionary[key] = values;
    }
  }
}
if (!dictionary) throw new Error('Could not read interface translations');
process.stdout.write(JSON.stringify(dictionary));
