import { renderMarkdown } from './reader';
import { catalog } from './catalog';

type Day = {day:number; id:string; chapter:number; week:number; study_day:number; date:string|null; title:string|null; state:string; exercise_ids:string[]};
type Plan = {months:number; reference_lessons:number; planned_daily_positions:number; mapped_draft_readings:number; native_daily_lessons:number; reviewed_daily_lessons:number; mapping_state:string; mapping_issue:string|null; days:Day[]; calendar:{first_study_date:string|null; period_end_exclusive:string|null; calendar_weekdays:number|null; sequence_end:string|null; alignment:string; difference_days?:number}};
type Unit = {id:string; chapter:number; title:string; markdown:string; example:string; exercises:{id:string;prompt:string;answer:string}[]; source_url:string; source_blob_sha:string; previous:number|null; next:number|null};
const $ = (id:string) => document.getElementById(id)!;
const params = new URLSearchParams(location.search);
const level = params.get('level') || 'rapid-1-month';
const area = params.get('area') || 'incident-response-resilience';
const language = params.get('lang') || 'en';
const start = params.get('start') || '';
const valid = catalog.level_order.includes(level) && catalog.languages.includes(language) && catalog.courses.some(c => c.level === level && c.area === area);
let plan:Plan|null = null, current = Number(params.get('day') || '1'), requestId = 0;
const labels:Record<string,string[]> = {
 en:['Day','Chapter','Planned — teaching not available','Mapped draft reading','Previous day','Next day','Worked example','Exercises','Reveal worked answer','Daily allocation still needs workload and editorial review.'],
 pt:['Dia','Capítulo','Planejada — conteúdo ainda indisponível','Leitura de rascunho mapeada','Dia anterior','Próximo dia','Exemplo comentado','Exercícios','Ver resposta comentada','A distribuição diária ainda precisa de revisão de carga de estudo e revisão editorial.'],
 es:['Día','Capítulo','Planificada — contenido no disponible','Lectura de borrador mapeada','Día anterior','Día siguiente','Ejemplo explicado','Ejercicios','Ver respuesta explicada','La distribución diaria requiere revisión de carga de estudio y revisión editorial.'],
 he:['יום','פרק','מתוכנן — התוכן עדיין אינו זמין','קריאה ממופה בטיוטה','היום הקודם','היום הבא','דוגמה מוסברת','תרגילים','הצגת פתרון מוסבר','חלוקת הלימוד היומית עדיין דורשת בדיקת עומס ועריכה.'],
 fr:['Jour','Chapitre','Prévu — contenu indisponible','Lecture de brouillon associée','Jour précédent','Jour suivant','Exemple expliqué','Exercices','Afficher la réponse expliquée','La répartition quotidienne nécessite une révision de la charge de travail et une révision éditoriale.'],
 ru:['День','Глава','Запланировано — материал недоступен','Чтение фрагмента черновика','Предыдущий день','Следующий день','Разобранный пример','Упражнения','Показать разбор ответа','Ежедневное распределение требует проверки нагрузки и редакционной проверки.'],
 de:['Tag','Kapitel','Geplant — Lehrtext nicht verfügbar','Zugeordnete Entwurfslektüre','Vorheriger Tag','Nächster Tag','Erläutertes Beispiel','Übungen','Erläuterte Antwort anzeigen','Die tägliche Aufteilung erfordert noch eine Prüfung des Lernaufwands und eine redaktionelle Prüfung.'],
 zh:['学习日','章节','已规划 — 内容尚未提供','已映射的草稿阅读','上一学习日','下一学习日','讲解示例','练习','显示答案解析','每日安排仍需学习负荷检查和编辑审查。'],
 ja:['学習日','章','計画済み — 本文は未提供','草稿に対応する読書範囲','前の学習日','次の学習日','解説付きの例','演習','解答と解説を表示','日々の配分には学習負荷と編集の確認が必要です。'],
};
const t = labels[language] || labels.en;
function link(text:string, href:string) { const node=document.createElement('a');node.className='button secondary';node.textContent=text;node.href=href;return node; }
function message(text:string) { $('daily-status').textContent=text; }
function address(day?:number) {const q=new URLSearchParams({level,area,lang:language});if(start)q.set('start',start);if(day)q.set('day',String(day));return '/daily/?'+q;}
function selectValue(id:string,value:string){( $(id) as HTMLInputElement).value=value;}
function weeks(){if(!plan)return; const select=$('daily-week') as HTMLSelectElement;select.replaceChildren();for(const week of [...new Set(plan.days.map(d=>d.week))]){const o=document.createElement('option');o.value=String(week);o.textContent=String(week);select.append(o);}select.onchange=()=>drawDays(Number(select.value));}
function drawDays(week:number){if(!plan)return;const nav=$('daily-days');nav.replaceChildren();for(const day of plan.days.filter(d=>d.week===week)){const b=document.createElement('button');b.type='button';b.className='button secondary';b.textContent=`${t[0]} ${day.day}${day.date?' · '+day.date:''} · ${day.state==='mapped-draft'?t[3]:t[2]}`;b.setAttribute('aria-current',day.day===current?'page':'false');b.onclick=()=>void open(day.day,true);nav.append(b);}}
async function renderSection(parent:HTMLElement,title:string,markdown:string,unit:Unit){const heading=document.createElement('h3');heading.textContent=title;const body=document.createElement('div');body.className='prose';parent.append(heading,body);await renderMarkdown(body,markdown,unit.source_url,language,'daily');}
async function open(day:number,push=false){
 if(!plan || !Number.isInteger(day) || day<1 || day>plan.days.length){message('Unknown study day.');return;}
 const id=++requestId;current=day;const selected=plan.days[day-1];selectValue('daily-week',String(selected.week));drawDays(selected.week);
 if(push)history.pushState(null,'',address(day));
 $('daily-title').textContent=`${t[0]} ${day} · ${selected.title || t[2]}`;
 $('daily-state').textContent=`${t[1]} ${selected.chapter} · ${selected.state==='mapped-draft'?t[3]:t[2]}`;
 $('daily-content').replaceChildren();const nav=$('daily-navigation');nav.replaceChildren();
 for(const [text,n] of [[t[4],day-1],[t[5],day+1]] as [string,number][]){if(n>=1&&n<=plan.days.length){const a=link(text,address(n));a.onclick=e=>{e.preventDefault();void open(n,true);};nav.append(a);}}
 if(selected.state!=='mapped-draft'){message(plan.mapping_state==='blocked'?'Mapping blocked: '+plan.mapping_issue:t[2]);return;}
 message('Loading the exact mapped source…');
 try{
  const response=await fetch(`/api/daily/${level}/${area}/${language}/${day}`);
  if(!response.ok)throw new Error(response.status===409?'The source changed. Mapping review is required.':'Daily text unavailable in this edition.');
  const unit=await response.json() as Unit;if(id!==requestId)return;
  // Render off-screen; an older asynchronous request must never overwrite a newer choice.
  const container=document.createElement('div');container.lang=language;container.dir=language==='he'?'rtl':'ltr';
  await renderSection(container,unit.title,unit.markdown,unit);
  await renderSection(container,t[6],unit.example,unit);
  const heading=document.createElement('h3');heading.textContent=t[7];container.append(heading);
  for(const exercise of unit.exercises){
   const prompt=document.createElement('div');prompt.className='prose';container.append(prompt);await renderMarkdown(prompt,exercise.prompt,unit.source_url,language,'daily');
   const details=document.createElement('details'),summary=document.createElement('summary'),answer=document.createElement('div');summary.textContent=`${exercise.id} · ${t[8]}`;answer.className='prose';details.append(summary,answer);container.append(details);
   await renderMarkdown(answer,exercise.answer,unit.source_url,language,'daily');
  }
  const provenance=document.createElement('p');provenance.textContent=`${t[9]} Source blob: ${unit.source_blob_sha}`;container.append(provenance,link('GitHub source',unit.source_url));
  if(id!==requestId)return;$('daily-content').replaceChildren(container);message(t[3]+' · '+t[9]);
 }catch(error){if(id===requestId)message(String(error));}
}
async function init(){
 if(!valid){message('Unknown course or language. Select a catalog entry; no alternative edition was substituted.');return;}
 selectValue('daily-level',level);selectValue('daily-area',area);selectValue('daily-language',language);selectValue('daily-start',start);
 try{
  const response=await fetch(`/api/daily/${level}/${area}/${language}`+(start?'?'+new URLSearchParams({start}):''));
  if(!response.ok)throw new Error('Daily plan unavailable; the new API may still require local deployment. This is not evidence that no teaching exists.');
  plan=await response.json() as Plan;
  $('daily-summary').textContent=`${plan.months} calendar month(s) · Monday–Friday · ${plan.reference_lessons} reference positions · ${plan.mapped_draft_readings} mapped draft readings · ${plan.native_daily_lessons} native daily lessons · ${plan.reviewed_daily_lessons} reviewed daily lessons. Planned positions: ${plan.planned_daily_positions}.`;
  const c=plan.calendar;$('daily-calendar').textContent=c.first_study_date?`First study: ${c.first_study_date}; calendar end (exclusive): ${c.period_end_exclusive}; weekdays in that period: ${c.calendar_weekdays}; fixed-sequence last date: ${c.sequence_end}. ${c.alignment==='aligned'?'Calendar counts align.':'Alignment review required: '+c.difference_days+' day(s) difference. No lessons were silently added, repeated or removed.'}`:'Undated reference plan. Choose a start to compare the fixed sequence with the actual calendar months. Holidays and recesses are not excluded.';
  $('daily-links').replaceChildren(link('Whole chapters',`/courses/${level}/${area}/?lang=${language}`),link('One full book',`/book/?${new URLSearchParams({level,area,lang:language})}`),link('Daily-study rules','/read/?path=DAILY_STUDY_STANDARD.md'));
  weeks();await open(current);
 }catch(error){message(String(error));}
}
window.addEventListener('popstate',()=>{const q=new URLSearchParams(location.search);if((q.get('level')||level)!==level||(q.get('area')||area)!==area||(q.get('lang')||language)!==language||(q.get('start')||'')!==start){location.reload();return;}void open(Number(q.get('day')||'1'));});
void init();
