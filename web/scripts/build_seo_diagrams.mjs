import { build } from 'esbuild';

await build({
  entryPoints: ['src/lib/seo-diagrams.js'],
  outfile: 'dist/seo-diagrams.js',
  bundle: true,
  minify: true,
  format: 'iife',
  target: 'es2022',
});
