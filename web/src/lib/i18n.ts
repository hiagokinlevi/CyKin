type Language = 'en' | 'pt' | 'es';

export function siteLanguage(): Language {
  const selected = document.documentElement.dataset.language;
  return selected === 'pt' || selected === 'es' ? selected : 'en';
}

// Interface text only. Course manuscripts and quoted reference documents retain
// the language of their published edition.
const copy: Record<string, [string, string]> = {
  'Skip to content': ['Pular para o conteúdo', 'Saltar al contenido'],
  'CyKin, home': ['CyKin, início', 'CyKin, inicio'],
  'Main navigation': ['Navegação principal', 'Navegación principal'],
  'Start here': ['Comece por aqui', 'Empieza aquí'],
  'Courses': ['Cursos', 'Cursos'],
  'Cybersecurity': ['Cibersegurança', 'Ciberseguridad'],
  'Information security': ['Segurança da informação', 'Seguridad de la información'],
  'Data governance': ['Governança de dados', 'Gobernanza de datos'],
  'Privacy and data protection': ['Privacidade e proteção de dados', 'Privacidad y protección de datos'],
  'Security governance, risk and compliance': ['Governança de segurança, risco e conformidade', 'Gobernanza de seguridad, riesgo y cumplimiento'],
  'Human factors and cyber policy': ['Fatores humanos e política cibernética', 'Factores humanos y política cibernética'],
  'Security architecture and engineering': ['Arquitetura e engenharia de segurança', 'Arquitectura e ingeniería de seguridad'],
  'Cryptography and trust services': ['Criptografia e serviços de confiança', 'Criptografía y servicios de confianza'],
  'Web3, blockchain and cryptoasset security': ['Segurança de Web3, blockchain e criptoativos', 'Seguridad de Web3, blockchain y criptoactivos'],
  'Identity and access management': ['Gestão de identidade e acesso', 'Gestión de identidad y acceso'],
  'Network and communications security': ['Segurança de redes e comunicações', 'Seguridad de redes y comunicaciones'],
  'Systems, endpoints and hardware security': ['Segurança de sistemas, dispositivos e hardware', 'Seguridad de sistemas, dispositivos y hardware'],
  'Cloud and container security': ['Segurança de nuvem e contêineres', 'Seguridad de nube y contenedores'],
  'Application and software supply chain security': ['Segurança de aplicações e cadeia de software', 'Seguridad de aplicaciones y cadena de software'],
  'Security operations and blue team': ['Operações de segurança e equipe azul', 'Operaciones de seguridad y equipo azul'],
  'Incident response and cyber resilience': ['Resposta a incidentes e resiliência cibernética', 'Respuesta a incidentes y resiliencia cibernética'],
  'Digital forensics and malware analysis': ['Perícia digital e análise de malware', 'Informática forense y análisis de malware'],
  'Threat intelligence and OSINT': ['Inteligência de ameaças e OSINT', 'Inteligencia de amenazas y OSINT'],
  'Authorized offensive security and red team': ['Segurança ofensiva autorizada e equipe vermelha', 'Seguridad ofensiva autorizada y equipo rojo'],
  'AI and machine-learning security': ['Segurança de IA e aprendizado de máquina', 'Seguridad de IA y aprendizaje automático'],
  'Quantum and post-quantum security': ['Segurança quântica e pós-quântica', 'Seguridad cuántica y poscuántica'],
  'OT, IoT and cyber-physical security': ['Segurança de OT, IoT e sistemas ciberfísicos', 'Seguridad de OT, IoT y sistemas ciberfísicos'],
  'Critical infrastructure and sector security': ['Segurança de infraestrutura crítica e setores', 'Seguridad de infraestructuras críticas y sectores'],
  'For AIs': ['Para IAs', 'Para IA'],
  'Editorial standard': ['Padrão editorial', 'Estándar editorial'],
  'Site language': ['Idioma do site', 'Idioma del sitio'],
  'Toggle light and dark theme': ['Alternar tema claro e escuro', 'Cambiar entre tema claro y oscuro'],
  'Toggle theme': ['Alternar tema', 'Cambiar tema'],
  'My area': ['Minha área', 'Mi área'],
  'Open learning library': ['Biblioteca de estudo aberta', 'Biblioteca de estudio abierta'],
  'Editorial responsibility: hiagokinlevi': ['Responsabilidade editorial: hiagokinlevi', 'Responsabilidad editorial: hiagokinlevi'],
  'Rights': ['Direitos', 'Derechos'],
  'Books and courses': ['Livros e cursos', 'Libros y cursos'],
  'OPEN LIBRARY · PUBLIC SOURCE': ['BIBLIOTECA ABERTA · FONTE PÚBLICA', 'BIBLIOTECA ABIERTA · FUENTE PÚBLICA'],
  'Learn to think about': ['Aprenda a pensar em', 'Aprende a pensar en'],
  'security': ['segurança', 'seguridad'],
  'clearly.': ['com clareza.', 'con claridad.'],
  'A journey through cybersecurity books, lessons and exercises for people and AI systems. Choose your path and study without an account.': ['Uma jornada por livros, aulas e exercícios de cibersegurança para pessoas e sistemas de IA. Escolha seu caminho e estude sem cadastro.', 'Un recorrido por libros, lecciones y ejercicios de ciberseguridad para personas y sistemas de IA. Elige tu camino y estudia sin registrarte.'],
  'Start learning': ['Começar a estudar', 'Empezar a estudiar'],
  'Connect an AI': ['Conectar uma IA', 'Conectar una IA'],
  'courses mapped': ['cursos no mapa', 'cursos en el mapa'],
  'subject areas': ['áreas de estudo', 'áreas de estudio'],
  'study levels': ['níveis de formação', 'niveles de estudio'],
  'Abstract illustration of learning paths': ['Ilustração das trilhas de aprendizagem', 'Ilustración de las rutas de aprendizaje'],
  'Knowledge': ['Conhecimento', 'Conocimiento'],
  'technical, open': ['técnico, aberto', 'técnico, abierto'],
  'One lesson per chapter': ['Uma aula por capítulo', 'Una lección por capítulo'],
  'with exercises': ['com exercícios', 'con ejercicios'],
  'Living source': ['Fonte viva', 'Fuente viva'],
  'books kept current': ['livros atualizados', 'libros actualizados'],
  'START HERE': ['COMECE POR AQUI', 'EMPIEZA AQUÍ'],
  'Two ways to find your next lesson.': ['Duas formas de chegar à próxima aula.', 'Dos maneras de encontrar tu próxima lección.'],
  'Choose your route. Both paths show every subject in order and open chapters that have teaching text.': ['Escolha sua trilha. Ambas mostram todas as matérias em ordem e abrem os capítulos com texto didático.', 'Elige tu ruta. Ambas muestran todas las materias en orden y abren los capítulos con contenido didáctico.'],
  'I have a subject in mind': ['Tenho um tema em mente', 'Tengo un tema en mente'],
  'Choose a language, subject and level. Open the course and follow its lessons in order.': ['Escolha idioma, tema e nível. Abra o curso e siga as aulas em ordem.', 'Elige idioma, tema y nivel. Abre el curso y sigue las lecciones en orden.'],
  'Language': ['Idioma', 'Idioma'],
  'Subject': ['Tema', 'Tema'],
  'Level': ['Nível', 'Nivel'],
  '1. Language': ['1. Idioma', '1. Idioma'],
  '2. Subject': ['2. Tema', '2. Tema'],
  '3. Level': ['3. Nível', '3. Nivel'],
  '2. Level': ['2. Nível', '2. Nivel'],
  'Open course': ['Abrir curso', 'Abrir curso'],
  'I want to study a whole level': ['Quero estudar um nível inteiro', 'Quiero estudiar un nivel completo'],
  'Choose a language and level. Browse all 23 subjects in curriculum order, with their lesson guides.': ['Escolha idioma e nível. Veja os 23 temas em ordem curricular, com seus guias de aula.', 'Elige idioma y nivel. Consulta los 23 temas en orden curricular, con sus guías de lecciones.'],
  '23 subjects': ['23 temas', '23 temas'],
  'Move from the first subject to the last, lesson by lesson, with each book in reach.': ['Avance do primeiro ao último tema, aula por aula, com cada livro ao alcance.', 'Avanza del primer al último tema, lección por lección, con cada libro a mano.'],
  'View all subjects': ['Ver todos os temas', 'Ver todos los temas'],
  'Loading the public catalog…': ['Carregando o catálogo público…', 'Cargando el catálogo público…'],
  'Catalog loaded. Each lesson is read from the current public manuscript.': ['Catálogo carregado. Cada aula vem do manuscrito público atual.', 'Catálogo cargado. Cada lección proviene del manuscrito público actual.'],
  'FROM CONCEPT TO PRACTICE': ['DO CONCEITO À PRÁTICA', 'DEL CONCEPTO A LA PRÁCTICA'],
  'Learning you can verify.': ['Aprendizado que você pode verificar.', 'Aprendizaje que puedes verificar.'],
  'Each subject is one chapter in its course book. The lesson page brings together explanations, examples, exercises and worked answers, with links to the previous chapter, index and next chapter.': ['Cada matéria é um capítulo do livro do curso. A página da aula reúne explicações, exemplos, exercícios e respostas comentadas, com links para o capítulo anterior, índice e próximo capítulo.', 'Cada materia es un capítulo del libro del curso. La página de la lección reúne explicaciones, ejemplos, ejercicios y respuestas desarrolladas, con enlaces al capítulo anterior, índice y siguiente capítulo.'],
  'Read the editorial standard →': ['Leia o padrão editorial →', 'Lee el estándar editorial →'],
  'Transparent source': ['Fonte transparente', 'Fuente transparente'],
  'Open text with its course and edition identified.': ['Texto aberto com curso e edição identificados.', 'Texto abierto con curso y edición identificados.'],
  'No entry barrier': ['Sem barreira de entrada', 'Sin barreras de acceso'],
  'Read courses, books and exercises without an account.': ['Leia cursos, livros e exercícios sem cadastro.', 'Lee cursos, libros y ejercicios sin registrarte.'],
  'Ready for other AIs': ['Pronto para outras IAs', 'Listo para otras IA'],
  'Public API, Markdown and read-only MCP server.': ['API pública, Markdown e servidor MCP de leitura.', 'API pública, Markdown y servidor MCP de solo lectura.'],
  'FOR SYSTEMS AND AGENTS': ['PARA SISTEMAS E AGENTES', 'PARA SISTEMAS Y AGENTES'],
  'A library other AIs can consult.': ['Uma biblioteca que outras IAs podem consultar.', 'Una biblioteca que otras IA pueden consultar.'],
  'ChatGPT, Claude, DAI and other tools can discover courses and read lessons through MCP or the open API. Every response identifies its public manuscript.': ['ChatGPT, Claude, DAI e outras ferramentas podem descobrir cursos e ler aulas por MCP ou pela API aberta. Cada resposta identifica seu manuscrito público.', 'ChatGPT, Claude, DAI y otras herramientas pueden descubrir cursos y leer lecciones por MCP o la API abierta. Cada respuesta identifica su manuscrito público.'],
  'Explore MCP access →': ['Explorar acesso MCP →', 'Explorar acceso MCP →'],
  'STUDY ROOM · OPEN ACCESS': ['SALA DE ESTUDO · ACESSO ABERTO', 'SALA DE ESTUDIO · ACCESO ABIERTO'],
  'Your path through knowledge.': ['Seu caminho pelo conhecimento.', 'Tu camino por el conocimiento.'],
  'Choose a route and move through the published lessons. Planned chapters are identified and never presented as finished lessons.': ['Escolha uma trilha e avance pelas aulas publicadas. Capítulos planejados são identificados e nunca apresentados como aulas prontas.', 'Elige una ruta y avanza por las lecciones publicadas. Los capítulos planificados se identifican y nunca se presentan como lecciones terminadas.'],
  'Route': ['Trilha', 'Ruta'],
  'Subject → level': ['Tema → nível', 'Tema → nivel'],
  'Level → all subjects': ['Nível → todos os temas', 'Nivel → todos los temas'],
  'Course and lesson guide': ['Guia de cursos e aulas', 'Guía de cursos y lecciones'],
  'COURSE GUIDE': ['GUIA DO CURSO', 'GUÍA DEL CURSO'],
  'Choose a route.': ['Escolha uma trilha.', 'Elige una ruta.'],
  'Choose a course to begin.': ['Escolha um curso para começar.', 'Elige un curso para empezar.'],
  'The guide shows subjects in order and marks chapters with published lesson text.': ['O guia mostra as matérias em ordem e marca os capítulos com aulas publicadas.', 'La guía muestra las materias en orden y marca los capítulos con lecciones publicadas.'],
  'View worked answers': ['Ver respostas comentadas', 'Ver respuestas desarrolladas'],
  'YOUR PROGRESS · OPTIONAL': ['SEU PROGRESSO · OPCIONAL', 'TU PROGRESO · OPCIONAL'],
  'Save this lesson': ['Salvar esta aula', 'Guardar esta lección'],
  'You can study without an account. With sign-in, mark lessons and save your answers.': ['Você pode estudar sem conta. Com login, marque aulas e salve respostas.', 'Puedes estudiar sin cuenta. Al iniciar sesión, marca lecciones y guarda respuestas.'],
  'Lessons in this course': ['Aulas neste curso', 'Lecciones de este curso'],
  '23 subjects in study order': ['23 temas na ordem de estudo', '23 temas en orden de estudio'],
  'Choose a level for this subject': ['Escolha um nível para este tema', 'Elige un nivel para este tema'],
  'Open published lesson': ['Abrir aula publicada', 'Abrir lección publicada'],
  'Planned chapter': ['Capítulo planejado', 'Capítulo planificado'],
  'Loading the course guide…': ['Carregando o guia do curso…', 'Cargando la guía del curso…'],
  'Loading the current course plan and book…': ['Carregando plano e livro atuais…', 'Cargando el plan y libro actuales…'],
  'Read the full book here →': ['Leia o livro completo aqui →', 'Lee el libro completo aquí →'],
  'Read the course plan here →': ['Leia o plano do curso aqui →', 'Lee el plan del curso aquí →'],
  'This course could not be loaded.': ['Não foi possível carregar este curso.', 'No se pudo cargar este curso.'],
  'This course is temporarily unavailable. Please try again shortly.': ['Curso temporariamente indisponível. Tente novamente em breve.', 'Curso temporalmente no disponible. Inténtalo de nuevo pronto.'],
  'Sign-in unavailable': ['Login indisponível', 'Inicio de sesión no disponible'],
  'Sign in to save progress →': ['Entre para salvar progresso →', 'Inicia sesión para guardar el progreso →'],
  'Mark lesson complete ✓': ['Marcar aula como concluída ✓', 'Marcar lección como completada ✓'],
  'Lesson completed and saved to your account.': ['Aula concluída e salva na sua conta.', 'Lección completada y guardada en tu cuenta.'],
  'Could not save right now.': ['Não foi possível salvar agora.', 'No se pudo guardar ahora.'],
  'Save your attempt, then compare the worked answer.': ['Salve sua tentativa e compare com a resposta comentada.', 'Guarda tu intento y compáralo con la respuesta desarrollada.'],
  'Save attempt': ['Salvar tentativa', 'Guardar intento'],
  'Read this chapter in the book →': ['Leia este capítulo no livro →', 'Lee este capítulo en el libro →'],
  'Read the chapter plan →': ['Leia o plano do capítulo →', 'Lee el plan del capítulo →'],
  'This subject is in the course plan. Its lesson text has not been published in this edition.': ['Esta matéria está no plano do curso. A aula ainda não foi publicada nesta edição.', 'Esta materia está en el plan del curso. La lección aún no se ha publicado en esta edición.'],
  'Loading the published lesson…': ['Carregando a aula publicada…', 'Cargando la lección publicada…'],
  'The lesson is temporarily unavailable.': ['Aula temporariamente indisponível.', 'Lección temporalmente no disponible.'],
  '← Previous lesson': ['← Aula anterior', '← Lección anterior'],
  'Course guide': ['Guia do curso', 'Guía del curso'],
  'Next lesson →': ['Próxima aula →', 'Siguiente lección →'],
  'Next course →': ['Próximo curso →', 'Siguiente curso →'],
  'Choose a course to read its public book.': ['Escolha um curso para ler seu livro público.', 'Elige un curso para leer su libro público.'],
  'The catalog is temporarily unavailable.': ['O catálogo está temporariamente indisponível.', 'El catálogo no está disponible temporalmente.'],
  'OPEN BOOK · NO ACCOUNT REQUIRED': ['LIVRO ABERTO · SEM CADASTRO', 'LIBRO ABIERTO · SIN REGISTRO'],
  'Public course book': ['Livro público do curso', 'Libro público del curso'],
  'Loading the current book…': ['Carregando o livro atual…', 'Cargando el libro actual…'],
  'Course lesson guide →': ['Guia de aulas do curso →', 'Guía de lecciones del curso →'],
  'CHAPTERS': ['CAPÍTULOS', 'CAPÍTULOS'],
  'Book chapters': ['Capítulos do livro', 'Capítulos del libro'],
  'Choose a course from the study guide.': ['Escolha um curso no guia de estudo.', 'Elige un curso en la guía de estudio.'],
  'The course guide could not be loaded.': ['Não foi possível carregar o guia do curso.', 'No se pudo cargar la guía del curso.'],
  'This edition has a plan, but its book has not been written yet.': ['Esta edição tem um plano, mas o livro ainda não foi escrito.', 'Esta edición tiene un plan, pero el libro aún no se ha escrito.'],
  'The book is temporarily unavailable.': ['O livro está temporariamente indisponível.', 'El libro no está disponible temporalmente.'],
  'OPEN REFERENCE': ['REFERÊNCIA ABERTA', 'REFERENCIA ABIERTA'],
  'Course reference': ['Referência do curso', 'Referencia del curso'],
  'Loading the document…': ['Carregando o documento…', 'Cargando el documento…'],
  'Browse courses →': ['Explorar cursos →', 'Explorar cursos →'],
  'Choose a document from a course page.': ['Escolha um documento na página do curso.', 'Elige un documento en la página del curso.'],
  'This reference is unavailable.': ['Esta referência está indisponível.', 'Esta referencia no está disponible.'],
  'Public document · linked course references open within CyKin.': ['Documento público · referências do curso abrem no CyKin.', 'Documento público · las referencias del curso se abren en CyKin.'],
  'LIBRARY FOR AIs': ['BIBLIOTECA PARA IAs', 'BIBLIOTECA PARA IA'],
  'Verifiable knowledge,': ['Conhecimento verificável,', 'Conocimiento verificable,'],
  'accessible by protocol.': ['acessível por protocolo.', 'accesible por protocolo.'],
  'CyKin offers the same books to human readers and agents. Discover courses, consult the index and read published chapters. Every result identifies its public source.': ['O CyKin oferece os mesmos livros a leitores e agentes. Descubra cursos, consulte o índice e leia capítulos publicados. Cada resultado identifica sua fonte pública.', 'CyKin ofrece los mismos libros a lectores y agentes. Descubre cursos, consulta el índice y lee capítulos publicados. Cada resultado identifica su fuente pública.'],
  'Explore lessons ↗': ['Explorar aulas ↗', 'Explorar lecciones ↗'],
  'Open OpenAPI ↗': ['Abrir OpenAPI ↗', 'Abrir OpenAPI ↗'],
  'Connect an agent': ['Conecte um agente', 'Conecta un agente'],
  'Use the public HTTP endpoint in an MCP client that accepts remote servers. Reading books requires no account or key.': ['Use o endpoint HTTP público em um cliente MCP que aceite servidores remotos. Ler livros não exige conta nem chave.', 'Usa el endpoint HTTP público en un cliente MCP que acepte servidores remotos. Leer libros no requiere cuenta ni clave.'],
  'Copy MCP URL': ['Copiar URL MCP', 'Copiar URL MCP'],
  'Copy': ['Copiar', 'Copiar'],
  'Copied': ['Copiado', 'Copiado'],
  'Tools:': ['Ferramentas:', 'Herramientas:'],
  'Resources: catalog and chapters.': ['Recursos: catálogo e capítulos.', 'Recursos: catálogo y capítulos.'],
  'Integrate without an SDK': ['Integre sem SDK', 'Integra sin SDK'],
  'The catalog and each lesson are available as JSON. Complete manuscripts are available as Markdown from the public editorial source.': ['O catálogo e cada aula estão disponíveis em JSON. Manuscritos completos estão disponíveis em Markdown da fonte editorial pública.', 'El catálogo y cada lección están disponibles en JSON. Los manuscritos completos están disponibles en Markdown desde la fuente editorial pública.'],
  'OpenAPI specification →': ['Especificação OpenAPI →', 'Especificación OpenAPI →'],
  'FROM COURSE TO CHAPTER': ['DO CURSO AO CAPÍTULO', 'DEL CURSO AL CAPÍTULO'],
  'Three steps to consult the library.': ['Três passos para consultar a biblioteca.', 'Tres pasos para consultar la biblioteca.'],
  'Discover': ['Descobrir', 'Descubrir'],
  'Locate': ['Localizar', 'Localizar'],
  'Read and cite': ['Ler e citar', 'Leer y citar'],
  'One source, open access.': ['Uma fonte, acesso aberto.', 'Una fuente, acceso abierto.'],
  'List the 207 courses and choose a language, subject and level. The catalog gives the structure; the book is checked again when a lesson opens.': ['Liste os 207 cursos e escolha idioma, tema e nível. O catálogo mostra a estrutura; o livro é verificado quando a aula abre.', 'Consulta los 207 cursos y elige idioma, tema y nivel. El catálogo muestra la estructura; el libro se comprueba al abrir la lección.'],
  'Browse subjects in study order. Each is marked as a published lesson or a planned chapter.': ['Percorra as matérias em ordem de estudo. Cada uma indica aula publicada ou capítulo planejado.', 'Recorre las materias en orden de estudio. Cada una indica lección publicada o capítulo planificado.'],
  'Read the lesson and worked answers. Use its public source URL when citing the original text.': ['Leia a aula e as respostas comentadas. Use a URL da fonte pública ao citar o texto original.', 'Lee la lección y las respuestas desarrolladas. Usa la URL de la fuente pública al citar el texto original.'],
  'The API reads manuscripts from the public': ['A API lê manuscritos da fonte pública', 'La API lee manuscritos de la fuente pública'],
  'branch. Changes to existing books appear without rebuilding the site. The catalog is generated when the site is published; new course structures need a new deployment. A published chapter does not mean the whole book passed editorial review.': ['. Alterações em livros existentes aparecem sem reconstruir o site. O catálogo é gerado na publicação; novas estruturas de curso precisam de novo deploy. Um capítulo publicado não significa que o livro inteiro passou por revisão editorial.', '. Los cambios en libros existentes aparecen sin reconstruir el sitio. El catálogo se genera al publicar; nuevas estructuras de cursos requieren otro despliegue. Un capítulo publicado no significa que el libro completo haya superado la revisión editorial.'],
  'Guide for agents ↗': ['Guia para agentes ↗', 'Guía para agentes ↗'],
  'Usage rights ↗': ['Direitos de uso ↗', 'Derechos de uso ↗'],
  'OPTIONAL STUDENT AREA': ['ÁREA OPCIONAL DO ESTUDANTE', 'ÁREA OPCIONAL DEL ESTUDIANTE'],
  'Your learning,': ['Seu estudo,', 'Tu aprendizaje,'],
  'at your pace.': ['no seu ritmo.', 'a tu ritmo.'],
  'Sign in only if you want to save completed lessons and exercise answers. Books, lessons and the API remain open without an account.': ['Entre apenas se quiser salvar aulas concluídas e respostas de exercícios. Livros, aulas e API continuam abertos sem conta.', 'Inicia sesión solo si quieres guardar lecciones completadas y respuestas a ejercicios. Libros, lecciones y API siguen abiertos sin cuenta.'],
  'IDENTITY': ['IDENTIDADE', 'IDENTIDAD'],
  'Checking access…': ['Verificando acesso…', 'Comprobando acceso…'],
  'YOUR STUDY AREA': ['SUA ÁREA DE ESTUDO', 'TU ÁREA DE ESTUDIO'],
  'Sign-in is managed by Cloudflare Access. CyKin does not store your password.': ['O login é gerenciado pelo Cloudflare Access. O CyKin não armazena sua senha.', 'El inicio de sesión lo gestiona Cloudflare Access. CyKin no guarda tu contraseña.'],
  'What you can track': ['O que você pode acompanhar', 'Qué puedes seguir'],
  'Completed lessons': ['Aulas concluídas', 'Lecciones completadas'],
  'Mark a chapter when you finish reading.': ['Marque um capítulo ao terminar a leitura.', 'Marca un capítulo cuando termines de leer.'],
  'Exercise attempts': ['Tentativas de exercícios', 'Intentos de ejercicios'],
  'Save your answers and continue later.': ['Salve suas respostas e continue depois.', 'Guarda tus respuestas y continúa después.'],
  'Audio and video': ['Áudio e vídeo', 'Audio y vídeo'],
  'Planned for a later stage; reading is already open.': ['Planejado para uma etapa futura; a leitura já está aberta.', 'Previsto para una etapa futura; la lectura ya está abierta.'],
  'MY HISTORY': ['MEU HISTÓRICO', 'MI HISTORIAL'],
  'Saved progress': ['Progresso salvo', 'Progreso guardado'],
  'Sign in to view your lessons and attempts.': ['Entre para ver suas aulas e tentativas.', 'Inicia sesión para ver tus lecciones e intentos.'],
  'Continue learning →': ['Continuar estudando →', 'Seguir estudiando →'],
  'Sign in with email →': ['Entrar com e-mail →', 'Iniciar sesión con correo →'],
  'Study without an account →': ['Estudar sem conta →', 'Estudiar sin cuenta →'],
  'Optional sign-in is not enabled on this domain yet.': ['O login opcional ainda não está ativado neste domínio.', 'El inicio de sesión opcional aún no está habilitado en este dominio.'],
  'Sign in to save progress.': ['Entre para salvar o progresso.', 'Inicia sesión para guardar el progreso.'],
  'Active session': ['Sessão ativa', 'Sesión activa'],
  'Your progress belongs only to your account.': ['Seu progresso pertence somente à sua conta.', 'Tu progreso pertenece solo a tu cuenta.'],
  'Progress could not be loaded now.': ['Não foi possível carregar o progresso agora.', 'No se pudo cargar el progreso ahora.'],
  'Completed': ['Concluída', 'Completada'],
  'In progress': ['Em andamento', 'En curso'],
  'No lessons marked yet. Begin with a published lesson.': ['Nenhuma aula marcada ainda. Comece por uma aula publicada.', 'Aún no hay lecciones marcadas. Comienza con una lección publicada.'],
  'Reading always open': ['Leitura sempre aberta', 'Lectura siempre abierta'],
  'Your history will appear when optional sign-in is available and you sign in.': ['Seu histórico aparecerá quando o login opcional estiver disponível e você entrar.', 'Tu historial aparecerá cuando el inicio de sesión opcional esté disponible y entres.'],
};

function dynamic(english: string, lang: Exclude<Language, 'en'>): string | null {
  const book = english.match(/^(\d+) written chapters · Read here or choose one lesson from the guide\.$/);
  if (book) return lang === 'pt' ? `${book[1]} capítulos escritos · Leia aqui ou escolha uma aula no guia.` : `${book[1]} capítulos escritos · Lee aquí o elige una lección de la guía.`;
  const published = english.match(/^(\d+) of (\d+) chapters have published lesson text in this edition\. A planned chapter may not yet have a lesson\.$/);
  if (published) return lang === 'pt' ? `${published[1]} de ${published[2]} capítulos têm aulas publicadas nesta edição. Um capítulo planejado pode ainda não ter aula.` : `${published[1]} de ${published[2]} capítulos tienen lecciones publicadas en esta edición. Un capítulo planificado puede no tener aún lección.`;
  const loaded = english.match(/^Guide updated for (.+)\.$/);
  if (loaded) return lang === 'pt' ? `Guia atualizado para ${loaded[1]}.` : `Guía actualizada para ${loaded[1]}.`;
  const lesson = english.match(/^Lesson (\d+) loaded from the public book\.$/);
  if (lesson) return lang === 'pt' ? `Aula ${lesson[1]} carregada do livro público.` : `Lección ${lesson[1]} cargada del libro público.`;
  const exercises = english.match(/^(\d+) exercise\(s\) found in this lesson · Public book edition$/);
  if (exercises) return lang === 'pt' ? `${exercises[1]} exercício(s) nesta aula · Edição pública do livro` : `${exercises[1]} ejercicio(s) en esta lección · Edición pública del libro`;
  return null;
}

export function ui(english: string): string {
  const pair = copy[english];
  const lang = siteLanguage();
  return lang === 'en' ? english : pair ? pair[lang === 'pt' ? 0 : 1] : dynamic(english, lang) || english;
}

function translateText(node: Text): void {
  const parent = node.parentElement;
  if (!parent || parent.closest('.prose, script, style, pre, code')) return;
  const raw = node.textContent || '';
  const value = raw.trim();
  if (!value) return;
  const translated = ui(value);
  if (translated !== value) node.textContent = raw.replace(value, translated);
}

function translateNode(root: Node): void {
  if (root.nodeType === Node.TEXT_NODE) { translateText(root as Text); return; }
  if (!(root instanceof Element)) return;
  if (root.closest('.prose, script, style, pre, code')) return;
  for (const name of ['aria-label', 'title', 'placeholder']) {
    const original = root.getAttribute(name);
    if (original) root.setAttribute(name, ui(original));
  }
  const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT);
  for (let current = walker.nextNode(); current; current = walker.nextNode()) translateText(current as Text);
  for (const element of root.querySelectorAll('[aria-label], [title], [placeholder]')) {
    for (const name of ['aria-label', 'title', 'placeholder']) {
      const original = element.getAttribute(name);
      if (original) element.setAttribute(name, ui(original));
    }
  }
}

export function translatePage(): void {
  if (siteLanguage() === 'en') return;
  translateNode(document.body);
  new MutationObserver(records => {
    for (const record of records) {
      if (record.type === 'characterData') translateNode(record.target);
      else for (const node of record.addedNodes) translateNode(node);
    }
  }).observe(document.body, { childList: true, characterData: true, subtree: true });
}
