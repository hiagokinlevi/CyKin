type Language = 'en' | 'pt' | 'es';

export function siteLanguage(): Language {
  const selected = document.documentElement.dataset.language;
  return selected === 'pt' || selected === 'es' ? selected : 'en';
}

export function editionLanguage(): string {
  const requested = new URLSearchParams(location.search).get('lang');
  return requested && ['en', 'pt', 'es', 'he', 'fr', 'ru', 'de', 'zh', 'ja'].includes(requested) ? requested : siteLanguage();
}

// Interface text only. Course manuscripts and quoted reference documents retain
// the language of their published edition.
const copy: Record<string, [string, string]> = {
  'Skip to content': ['Pular para o conteúdo', 'Saltar al contenido'],
  'CyKin, home': ['CyKin, início', 'CyKin, inicio'],
  'Main navigation': ['Navegação principal', 'Navegación principal'],
  'Start here': ['Comece por aqui', 'Empieza aquí'],
  'Courses': ['Cursos', 'Cursos'],
  'Browse courses': ['Explorar cursos', 'Explorar cursos'],
  'By level': ['Por nível', 'Por nivel'],
  'By subject': ['Por tema', 'Por tema'],
  'All levels →': ['Todos os níveis →', 'Todos los niveles →'],
  'All subjects →': ['Todos os temas →', 'Todos los temas →'],
  'Choose a level, then a course': ['Escolha um nível e depois um curso', 'Elige un nivel y luego un curso'],
  'Choose a subject, then a level': ['Escolha um tema e depois um nível', 'Elige un tema y luego un nivel'],
  'Loading courses…': ['Carregando cursos…', 'Cargando cursos…'],
  'View this group →': ['Ver este grupo →', 'Ver este grupo →'],
  'Rapid course': ['Curso rápido', 'Curso rápido'],
  'Professional': ['Profissionalizante', 'Profesional'],
  'Technical': ['Técnico', 'Técnico'],
  'Technologist': ['Tecnólogo', 'Tecnólogo'],
  "Bachelor's": ['Graduação', 'Grado'],
  'Engineering': ['Engenharia', 'Ingeniería'],
  'Postgraduate': ['Pós-graduação', 'Posgrado'],
  "Master's": ['Mestrado', 'Máster'],
  'Doctoral research': ['Pesquisa doutoral', 'Investigación doctoral'],
  'COURSE DIRECTORY': ['DIRETÓRIO DE CURSOS', 'DIRECTORIO DE CURSOS'],
  'Browse by level.': ['Explore por nível.', 'Explora por nivel.'],
  'Browse by subject.': ['Explore por tema.', 'Explora por tema.'],
  'Choose a level, then open one of its 23 separate courses. Every course has its own lesson guide and book.': ['Escolha um nível e abra um dos 23 cursos separados. Cada curso tem seu guia de aulas e livro.', 'Elige un nivel y abre uno de sus 23 cursos independientes. Cada curso tiene su guía de lecciones y libro.'],
  'Choose a subject, then a level. Each combination opens its own course and lessons.': ['Escolha um tema e depois um nível. Cada combinação abre seu próprio curso e aulas.', 'Elige un tema y luego un nivel. Cada combinación abre su propio curso y lecciones.'],
  '23 separate courses · Choose a subject and open its lessons.': ['23 cursos separados · Escolha um tema e abra as aulas.', '23 cursos separados · Elige un tema y abre las lecciones.'],
  '9 separate study levels · Choose the course that fits you.': ['9 níveis separados · Escolha o curso para você.', '9 niveles separados · Elige el curso adecuado.'],
  'Explore courses →': ['Explorar cursos →', 'Explorar cursos →'],
  'Choose a level →': ['Escolher nível →', 'Elegir nivel →'],
  'Levels': ['Níveis', 'Niveles'],
  'Subjects': ['Temas', 'Temas'],
  'All levels': ['Todos os níveis', 'Todos los niveles'],
  'All subjects': ['Todos os temas', 'Todos los temas'],
  'Browse by level': ['Explorar por nível', 'Explorar por nivel'],
  'Browse by subject': ['Explorar por tema', 'Explorar por tema'],
  'Each subject below is a separate course with its own book and lesson navigation. Follow the curriculum order or choose the subject you need.': ['Cada tema abaixo é um curso separado, com livro e navegação de aulas próprios. Siga a ordem curricular ou escolha o tema desejado.', 'Cada tema es un curso independiente, con libro y navegación de lecciones propios. Sigue el orden curricular o elige el tema que necesites.'],
  'Choose your level. Each course has its own chapter list, book and lesson navigation.': ['Escolha seu nível. Cada curso tem sua lista de capítulos, livro e navegação de aulas.', 'Elige tu nivel. Cada curso tiene su lista de capítulos, libro y navegación de lecciones.'],
  'Open course →': ['Abrir curso →', 'Abrir curso →'],
  'Previous level': ['Nível anterior', 'Nivel anterior'],
  'Next level →': ['Próximo nível →', 'Siguiente nivel →'],
  '← Previous course': ['← Curso anterior', '← Curso anterior'],
  'All courses at this level': ['Todos os cursos deste nível', 'Todos los cursos de este nivel'],
  'All courses at this level →': ['Todos os cursos deste nível →', 'Todos los cursos de este nivel →'],
  'Other levels in this subject →': ['Outros níveis deste tema →', 'Otros niveles de este tema →'],
  'Course language': ['Idioma do curso', 'Idioma del curso'],
  'COURSE CONTENTS': ['CONTEÚDO DO CURSO', 'CONTENIDO DEL CURSO'],
  'Modules and lessons': ['Módulos e aulas', 'Módulos y lecciones'],
  'Chapters and lessons': ['Capítulos e aulas', 'Capítulos y lecciones'],
  'Open each chapter to find its daily lessons.': ['Abra cada capítulo para encontrar as aulas diárias.', 'Abre cada capítulo para encontrar las lecciones diarias.'],
  'Published chapters and current curriculum blocks.': ['Capítulos publicados e blocos curriculares atuais.', 'Capítulos publicados y bloques curriculares actuales.'],
  'WEEKDAY STUDY PLAN': ['PLANO DE ESTUDO EM DIAS ÚTEIS', 'PLAN DE ESTUDIO DE LUNES A VIERNES'],
  'HOW TO STUDY': ['COMO ESTUDAR', 'CÓMO ESTUDIAR'],
  'One idea, taught properly': ['Uma ideia, ensinada com rigor', 'Una idea, enseñada con rigor'],
  'Minimum lessons, no maximum': ['Mínimo de aulas, sem máximo', 'Mínimo de lecciones, sin máximo'],
  'Study one lesson on a weekday. The planning minimum for this level is a floor. If an idea needs another lesson to be taught well, the course grows. Chapter length follows the idea.': ['Estude uma aula por dia útil. O mínimo deste nível é um piso. Se uma ideia precisar de outra aula para ser bem ensinada, o curso cresce. O tamanho do capítulo segue a ideia.', 'Estudia una lección por día hábil. El mínimo de este nivel es un piso. Si una idea necesita otra lección para enseñarse bien, el curso crece. El tamaño del capítulo sigue la idea.'],
  'English lessons first': ['Aulas em inglês primeiro', 'Lecciones en inglés primero'],
  'A lesson is as long as the idea needs. Read the explanation, follow the worked example, then try the exercise. There is no required chapter length or lesson quota.': ['A aula tem o tamanho que a ideia pede. Leia a explicação, acompanhe o exemplo resolvido e faça o exercício. Não há tamanho obrigatório nem cota de aulas.', 'La lección tiene el tamaño que la idea pide. Lee la explicación, sigue el ejemplo resuelto y haz el ejercicio. No hay tamaño obligatorio ni cuota de lecciones.'],
  'Length follows the idea': ['O tamanho segue a ideia', 'El tamaño sigue la idea'],
  'English first, then translation': ['Inglês primeiro, depois a tradução', 'Inglés primero, luego la traducción'],
  'One chapter each Monday–Friday: learn the concept, follow a worked example, then solve an exercise. The plan applies to every language edition.': ['Um capítulo de segunda a sexta: aprenda o conceito, acompanhe um exemplo resolvido e faça um exercício. O plano vale para todos os idiomas.', 'Un capítulo de lunes a viernes: aprende el concepto, sigue un ejemplo resuelto y haz un ejercicio. El plan se aplica a todos los idiomas.'],
  'One lesson each Monday–Friday, normally five lessons in a weekly chapter. Learn the concept, follow a worked example, then solve an exercise. The plan applies to every language edition.': ['Uma aula por dia útil, normalmente cinco aulas em cada capítulo semanal. Aprenda o conceito, acompanhe um exemplo resolvido e faça um exercício. O plano vale para todos os idiomas.', 'Una lección por día hábil, normalmente cinco lecciones en cada capítulo semanal. Aprende el concepto, sigue un ejemplo resuelto y resuelve un ejercicio. El plan se aplica a todos los idiomas.'],
  'Mon': ['Seg', 'Lun'], 'Tue': ['Ter', 'Mar'], 'Wed': ['Qua', 'Mié'], 'Thu': ['Qui', 'Jue'], 'Fri': ['Sex', 'Vie'],
  'One course, one book. The study target is one chapter each weekday, with a worked example and an exercise. Read the chapters already published below.': ['Um curso, um livro. A meta é um capítulo por dia útil, com exemplo resolvido e exercício. Leia abaixo os capítulos já publicados.', 'Un curso, un libro. La meta es un capítulo por día hábil, con ejemplo resuelto y ejercicio. Lee abajo los capítulos ya publicados.'],
  'One course, one book. Study one lesson each weekday, normally in a weekly chapter with five lessons. Each lesson has a worked example and an exercise. Read what is published below.': ['Um curso, um livro. Estude uma aula por dia útil, normalmente em um capítulo semanal de cinco aulas. Cada aula traz um exemplo resolvido e um exercício. Leia abaixo o que já foi publicado.', 'Un curso, un libro. Estudia una lección por día hábil, normalmente en un capítulo semanal de cinco lecciones. Cada lección incluye un ejemplo resuelto y un ejercicio. Lee lo ya publicado.'],
  'Follow the subjects in their curricular order.': ['Siga as matérias na ordem curricular.', 'Sigue las materias en orden curricular.'],
  '← Course overview': ['← Visão geral do curso', '← Vista general del curso'],
  'Course overview': ['Visão geral do curso', 'Vista general del curso'],
  'Your course roadmap': ['Seu roteiro do curso', 'Tu recorrido del curso'],
  'Read lesson →': ['Ler aula →', 'Leer lección →'],
  'Not published': ['Ainda não publicada', 'Aún no publicada'],
  'This lesson has not been published in this edition yet. Choose another available lesson or return to the course overview.': ['Esta aula ainda não foi publicada nesta edição. Escolha outra aula disponível ou volte à visão geral do curso.', 'Esta lección aún no se ha publicado en esta edición. Elige otra disponible o vuelve a la vista general del curso.'],
  'Jump to exercises ↓': ['Ir para os exercícios ↓', 'Ir a los ejercicios ↓'],
  'One course, one book. Read its lessons in order, or open the full book. Each lesson keeps its exercises and worked answers together.': ['Um curso, um livro. Leia as aulas em ordem ou abra o livro completo. Cada aula reúne exercícios e respostas comentadas.', 'Un curso, un libro. Lee las lecciones en orden o abre el libro completo. Cada lección reúne ejercicios y respuestas desarrolladas.'],
  'Choose a chapter to read on this page.': ['Escolha um capítulo para ler nesta página.', 'Elige un capítulo para leer en esta página.'],
  'Loading this course…': ['Carregando este curso…', 'Cargando este curso…'],
  'Loading the current book and lesson guide…': ['Carregando livro e guia de aulas atuais…', 'Cargando libro y guía de lecciones actuales…'],
  'Course guide loaded.': ['Guia do curso carregado.', 'Guía del curso cargada.'],
  'Start first published lesson →': ['Começar pela primeira aula publicada →', 'Comenzar por la primera lección publicada →'],
  'Choose a course.': ['Escolha um curso.', 'Elige un curso.'],
  'Use the level menu to see all subjects at one study level, or the subject menu to compare that subject across levels. Each course opens on its own page.': ['Use o menu por nível para ver todos os temas de um nível, ou o menu por tema para comparar os níveis desse tema. Cada curso abre em sua própria página.', 'Usa el menú por nivel para ver todos los temas de un nivel, o el menú por tema para comparar sus niveles. Cada curso se abre en su propia página.'],
  '← Previous level': ['← Nível anterior', '← Nivel anterior'],
  '23 separate courses': ['23 cursos separados', '23 cursos separados'],
  '9 separate courses': ['9 cursos separados', '9 cursos separados'],
  'Browse all courses': ['Explore todos os cursos', 'Explora todos los cursos'],
  'Choose a course using the menus above.': ['Escolha um curso nos menus acima.', 'Elige un curso en los menús de arriba.'],
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
  'One lesson each weekday': ['Uma aula por dia útil', 'Una lección por día hábil'],
  'five in a weekly chapter': ['cinco em um capítulo semanal', 'cinco en un capítulo semanal'],
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
  'Each course has one book. Subjects organize modules, and the study target is one chapter every weekday, with a worked example and an exercise. The reader shows what is published and keeps previous, index and next navigation close to each lesson.': ['Cada curso tem um livro. As matérias organizam módulos; a meta é um capítulo por dia útil, com exemplo resolvido e exercício. O leitor mostra o que foi publicado e mantém a navegação entre aulas.', 'Cada curso tiene un libro. Las materias organizan módulos; la meta es un capítulo por día hábil, con ejemplo resuelto y ejercicio. El lector muestra lo publicado y mantiene la navegación entre lecciones.'],
  'Each course has one book. Subjects organize modules, weekly chapters group daily lessons, and each lesson has a worked example and an exercise. The reader shows what is published and keeps previous, index and next navigation close to each lesson.': ['Cada curso tem um livro. As matérias organizam módulos, os capítulos semanais reúnem aulas diárias e cada aula tem exemplo resolvido e exercício. O leitor mostra o que foi publicado e mantém a navegação entre aulas.', 'Cada curso tiene un libro. Las materias organizan módulos, los capítulos semanales reúnen lecciones diarias y cada lección tiene un ejemplo resuelto y un ejercicio. El lector muestra lo publicado y mantiene la navegación entre lecciones.'],
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
  'CHAPTERS & LESSONS': ['CAPÍTULOS E AULAS', 'CAPÍTULOS Y LECCIONES'],
  'Book chapters and lessons': ['Capítulos e aulas do livro', 'Capítulos y lecciones del libro'],
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
  const chapterLessonPosition = english.match(/^Chapter (\d+) · (.+) · Lesson (\d+) of (\d+)$/);
  if (chapterLessonPosition) return `${lang === 'pt' ? 'Capítulo' : 'Capítulo'} ${chapterLessonPosition[1]} · ${chapterLessonPosition[2]} · ${lang === 'pt' ? 'Aula' : 'Lección'} ${chapterLessonPosition[3]} de ${chapterLessonPosition[4]}`;
  const chapterLabel = english.match(/^Chapter (\d+) · (.+)$/);
  if (chapterLabel) return `Capítulo ${chapterLabel[1]} · ${chapterLabel[2]}`;
  const weeklyChapters = english.match(/^(\d+) weekly chapters planned$/);
  if (weeklyChapters) return lang === 'pt' ? `${weeklyChapters[1]} capítulos semanais previstos` : `${weeklyChapters[1]} capítulos semanales previstos`;
  const chaptersPublished = english.match(/^(\d+) chapters published$/);
  if (chaptersPublished) return `${chaptersPublished[1]} capítulos publicados`;
  const lessonsPublished = english.match(/^(\d+) daily lessons published$/);
  if (lessonsPublished) return lang === 'pt' ? `${lessonsPublished[1]} aulas diárias publicadas` : `${lessonsPublished[1]} lecciones diarias publicadas`;
  const chapterAvailability = english.match(/^(\d+) chapters and (\d+) of (\d+) indexed daily lessons published in this edition\.$/);
  if (chapterAvailability) return lang === 'pt' ? `${chapterAvailability[1]} capítulos e ${chapterAvailability[2]} de ${chapterAvailability[3]} aulas diárias indexadas publicados nesta edição.` : `${chapterAvailability[1]} capítulos y ${chapterAvailability[2]} de ${chapterAvailability[3]} lecciones diarias indexadas publicados en esta edición.`;
  const legacyChapterAvailability = english.match(/^(\d+) current subject chapters published\. Distinct daily lessons have not yet been indexed for this edition; the (\d+)-lesson baseline is a plan, not published content\.$/);
  if (legacyChapterAvailability) return lang === 'pt' ? `${legacyChapterAvailability[1]} capítulos antigos de matérias publicados. Aulas diárias distintas ainda não foram indexadas nesta edição; a base de ${legacyChapterAvailability[2]} aulas é um plano, não conteúdo publicado.` : `${legacyChapterAvailability[1]} capítulos anteriores de materias publicados. Aún no se han indexado lecciones diarias distintas en esta edición; la base de ${legacyChapterAvailability[2]} lecciones es un plan, no contenido publicado.`;
  const dailyIntro = english.match(/^(\d+) chapters and (\d+) daily lessons are published in this edition\.$/);
  if (dailyIntro) return lang === 'pt' ? `${dailyIntro[1]} capítulos e ${dailyIntro[2]} aulas diárias estão publicados nesta edição.` : `${dailyIntro[1]} capítulos y ${dailyIntro[2]} lecciones diarias están publicados en esta edición.`;
  const legacyIntro = english.match(/^(\d+) legacy subject chapters are published\. The daily lessons are still being developed\.$/);
  if (legacyIntro) return lang === 'pt' ? `${legacyIntro[1]} capítulos antigos de matérias estão publicados. As aulas diárias ainda estão em desenvolvimento.` : `${legacyIntro[1]} capítulos anteriores de materias están publicados. Las lecciones diarias siguen en desarrollo.`;
  const bookDaily = english.match(/^(\d+) written chapters · (\d+) daily lessons · Read here or choose one lesson from the guide\.$/);
  if (bookDaily) return lang === 'pt' ? `${bookDaily[1]} capítulos escritos · ${bookDaily[2]} aulas diárias · Leia aqui ou escolha uma aula no guia.` : `${bookDaily[1]} capítulos escritos · ${bookDaily[2]} lecciones diarias · Lee aquí o elige una lección de la guía.`;
  const bookLegacy = english.match(/^(\d+) legacy subject chapters · Read here or open the course guide\.$/);
  if (bookLegacy) return lang === 'pt' ? `${bookLegacy[1]} capítulos antigos de matérias · Leia aqui ou abra o guia do curso.` : `${bookLegacy[1]} capítulos anteriores de materias · Lee aquí o abre la guía del curso.`;
  const bareModule = english.match(/^Module (\d+)$/);
  if (bareModule) return `Módulo ${bareModule[1]}`;
  const weeks = english.match(/^(\d+) instructional weeks$/);
  if (weeks) return lang === 'pt' ? `${weeks[1]} semanas letivas` : `${weeks[1]} semanas lectivas`;
  const target = english.match(/^(\d+) daily lessons planned$/);
  if (target) return lang === 'pt' ? `${target[1]} aulas diárias previstas` : `${target[1]} lecciones diarias previstas`;
  const current = english.match(/^(\d+) current chapters published$/);
  if (current) return lang === 'pt' ? `${current[1]} capítulos atuais publicados` : `${current[1]} capítulos actuales publicados`;
  const publishedLessons = english.match(/^(\d+) lessons published$/);
  if (publishedLessons) return lang === 'pt' ? `${publishedLessons[1]} aulas publicadas` : `${publishedLessons[1]} lecciones publicadas`;
  const publishedNote = english.match(/^(\d+) lessons published in this edition\. An outline is not a lesson\.$/);
  if (publishedNote) return lang === 'pt' ? `${publishedNote[1]} aulas publicadas nesta edição. Um plano não é uma aula.` : `${publishedNote[1]} lecciones publicadas en esta edición. Un plan no es una lección.`;
  const publishedMinimum = english.match(/^(\d+) lessons published in this edition\. Planning minimum: (\d+)\. An outline is not a lesson\.$/);
  if (publishedMinimum) return lang === 'pt' ? `${publishedMinimum[1]} aulas publicadas nesta edição. Mínimo de planejamento: ${publishedMinimum[2]}. Um plano não é uma aula.` : `${publishedMinimum[1]} lecciones publicadas en esta edición. Mínimo de planificación: ${publishedMinimum[2]}. Un plan no es una lección.`;
  const planningMinimum = english.match(/^Planning minimum (\d+)$/);
  if (planningMinimum) return lang === 'pt' ? `Mínimo de planejamento ${planningMinimum[1]}` : `Mínimo de planificación ${planningMinimum[1]}`;
  const indexWithMinimum = english.match(/^(\d+) chapters in the current index · minimum (\d+)$/);
  if (indexWithMinimum) return lang === 'pt' ? `${indexWithMinimum[1]} capítulos no índice atual · mínimo ${indexWithMinimum[2]}` : `${indexWithMinimum[1]} capítulos en el índice actual · mínimo ${indexWithMinimum[2]}`;
  const indexChapters = english.match(/^(\d+) chapters in the current index$/);
  if (indexChapters) return lang === 'pt' ? `${indexChapters[1]} capítulos no índice atual` : `${indexChapters[1]} capítulos en el índice actual`;
  const directoryTarget = english.match(/^(\d+) weekday lessons planned · (\d+) current curriculum chapters$/);
  if (directoryTarget) return lang === 'pt' ? `${directoryTarget[1]} aulas por dia útil previstas · ${directoryTarget[2]} capítulos curriculares atuais` : `${directoryTarget[1]} lecciones por día hábil previstas · ${directoryTarget[2]} capítulos curriculares actuales`;
  const weeklyTitle = english.match(/^(\d+) weeks · (\d+) daily lessons$/);
  if (weeklyTitle) return lang === 'pt' ? `${weeklyTitle[1]} semanas · ${weeklyTitle[2]} aulas diárias` : `${weeklyTitle[1]} semanas · ${weeklyTitle[2]} lecciones diarias`;
  const dailyAvailability = english.match(/^(\d+) of (\d+) daily chapters published in this edition\. Unpublished lessons are not available yet\.$/);
  if (dailyAvailability) return lang === 'pt' ? `${dailyAvailability[1]} de ${dailyAvailability[2]} capítulos diários publicados nesta edição. Aulas não publicadas ainda não estão disponíveis.` : `${dailyAvailability[1]} de ${dailyAvailability[2]} capítulos diarios publicados en esta edición. Las lecciones no publicadas aún no están disponibles.`;
  const legacyAvailability = english.match(/^(\d+) current chapters published\. These older subject chapters are not yet the (\d+) distinct daily lessons required by the new schedule\.$/);
  if (legacyAvailability) return lang === 'pt' ? `${legacyAvailability[1]} capítulos atuais publicados. Esses capítulos antigos de matérias ainda não são as ${legacyAvailability[2]} aulas diárias distintas exigidas pelo novo plano.` : `${legacyAvailability[1]} capítulos actuales publicados. Estos capítulos antiguos de materias aún no son las ${legacyAvailability[2]} lecciones diarias distintas exigidas por el nuevo plan.`;
  const introLegacy = english.match(/^(\d+) current chapters are published\. Daily chapters are being developed toward the (\d+)-lesson target\.$/);
  if (introLegacy) return lang === 'pt' ? `${introLegacy[1]} capítulos atuais publicados. As aulas diárias estão em desenvolvimento rumo à meta de ${introLegacy[2]}.` : `${introLegacy[1]} capítulos actuales publicados. Las lecciones diarias están en desarrollo hacia la meta de ${introLegacy[2]}.`;
  const module = english.match(/^Module (\d+) · (Week|Month|Semester|Term|Year|Module) \d+$/);
  if (module) {
    const names: Record<string, [string, string]> = { Week: ['Semana', 'Semana'], Month: ['Mês', 'Mes'], Semester: ['Semestre', 'Semestre'], Term: ['Período', 'Período'], Year: ['Ano', 'Año'], Module: ['Módulo', 'Módulo'] };
    const kind = names[module[2]][lang === 'pt' ? 0 : 1];
    return `${lang === 'pt' ? 'Módulo' : 'Módulo'} ${module[1]} · ${kind} ${module[1]}`;
  }
  const moduleLesson = english.match(/^Module (\d+) · (Week|Month|Semester|Term|Year|Module) \d+ · Lesson (\d+) of (\d+)$/);
  if (moduleLesson) {
    const label = dynamic(`Module ${moduleLesson[1]} · ${moduleLesson[2]} ${moduleLesson[1]}`, lang);
    return `${label} · ${lang === 'pt' ? 'Aula' : 'Lección'} ${moduleLesson[3]} ${lang === 'pt' ? 'de' : 'de'} ${moduleLesson[4]}`;
  }
  const simpleLesson = english.match(/^Lesson (\d+) of (\d+)$/);
  if (simpleLesson) return lang === 'pt' ? `Aula ${simpleLesson[1]} de ${simpleLesson[2]}` : `Lección ${simpleLesson[1]} de ${simpleLesson[2]}`;
  const moduleCount = english.match(/^(\d+) modules$/);
  if (moduleCount) return `${moduleCount[1]} módulos`;
  const lessonCount = english.match(/^(\d+) lessons$/);
  if (lessonCount) return lang === 'pt' ? `${lessonCount[1]} aulas` : `${lessonCount[1]} lecciones`;
  const availableCount = english.match(/^(\d+) lessons available$/);
  if (availableCount) return lang === 'pt' ? `${availableCount[1]} aulas disponíveis` : `${availableCount[1]} lecciones disponibles`;
  const availableModule = english.match(/^(\d+) of (\d+) lessons available$/);
  if (availableModule) return lang === 'pt' ? `${availableModule[1]} de ${availableModule[2]} aulas disponíveis` : `${availableModule[1]} de ${availableModule[2]} lecciones disponibles`;
  const exerciseCount = english.match(/^(\d+) exercises · Worked answers below$/);
  if (exerciseCount) return lang === 'pt' ? `${exerciseCount[1]} exercícios · Respostas comentadas abaixo` : `${exerciseCount[1]} ejercicios · Respuestas desarrolladas abajo`;
  const levelDirectory = english.match(/^LEVEL (\d{2}) · 23 COURSES$/);
  if (levelDirectory) return lang === 'pt' ? `NÍVEL ${levelDirectory[1]} · 23 CURSOS` : `NIVEL ${levelDirectory[1]} · 23 CURSOS`;
  const subjectDirectory = english.match(/^SUBJECT · 9 SEPARATE COURSES$/);
  if (subjectDirectory) return lang === 'pt' ? 'TEMA · 9 CURSOS SEPARADOS' : 'TEMA · 9 CURSOS SEPARADOS';
  const levelCourse = english.match(/^LEVEL (\d{2}) · COURSE (\d{3})$/);
  if (levelCourse) return lang === 'pt' ? `NÍVEL ${levelCourse[1]} · CURSO ${levelCourse[2]}` : `NIVEL ${levelCourse[1]} · CURSO ${levelCourse[2]}`;
  const numbering = english.match(/^(LEVEL|COURSE|SUBJECT) (\d{2,3})( ·)?$/);
  if (numbering) return `${({ LEVEL: lang === 'pt' ? 'NÍVEL' : 'NIVEL', COURSE: 'CURSO', SUBJECT: 'TEMA' } as Record<string, string>)[numbering[1]]} ${numbering[2]}${numbering[3] || ''}`;
  const plannedLessons = english.match(/^(\d+) lessons in (?:the course guide|this course)$/);
  if (plannedLessons) return lang === 'pt' ? `${plannedLessons[1]} aulas neste curso` : `${plannedLessons[1]} lecciones en este curso`;
  const answer = english.match(/^Your answer for (EX\d+)$/);
  if (answer) return lang === 'pt' ? `Sua resposta para ${answer[1]}` : `Tu respuesta para ${answer[1]}`;
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
