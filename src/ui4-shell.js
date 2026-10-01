const PAGES=[
 ['app.html','home','Home','<path d="M3 11l9-8 9 8"/><path d="M5 10v10h14V10"/>'],
 ['focus.html','focus','Focus','<circle cx="12" cy="12" r="9"/><path d="M10 8l6 4-6 4z"/>'],
 ['queue.html','study','Study','<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="3"/>'],
 ['practice.html','practice','Practice','<path d="M4 20l4-1 11-11-3-3L5 16z"/><path d="M14 6l3 3"/>'],
 ['revision.html','review','Review','<path d="M20 7v5h-5"/><path d="M19 12a7 7 0 10-2 5"/>'],
 ['analytics.html','progress','Progress','<path d="M4 20V10m6 10V4m6 16v-7m5 7H2"/>'],
 ['cloud.html','cloud','Cloud','<path d="M7 18h11a4 4 0 000-8 6 6 0 00-11-2 5 5 0 000 10z"/>'],
 ['index.html','evidence','Evidence','<path d="M12 3l9 5-9 5-9-5z"/><path d="M3 12l9 5 9-5M3 16l9 5 9-5"/>']
];
const here=location.pathname.split('/').pop()||'index.html';
const icon=p=>`<svg viewBox="0 0 24 24" aria-hidden="true">${p}</svg>`;
const links=PAGES.map(x=>`<a class="${x[0]===here?'active':''}" href="./${x[0]}">${icon(x[3])}<span>${x[2]}</span></a>`).join('');
const side=document.createElement('aside');side.className='sp-sidebar';side.innerHTML=`<a class="sp-brand" href="./app.html"><span class="sp-brand-mark">S</span><span><strong>SmartPrep</strong><small>Personal study OS</small></span></a><nav class="sp-nav">${links}</nav><div class="sp-side-foot"><button data-sp-theme>◐ Switch theme</button><a href="./cloud.html">● Sync status</a></div>`;document.body.prepend(side);
const tools=document.createElement('div');tools.className='sp-top-tools';tools.innerHTML='<button class="sp-menu" aria-label="Open navigation">☰</button><button data-sp-theme aria-label="Switch theme">◐</button>';document.body.append(tools);
const mobile=document.createElement('nav');mobile.className='sp-mobile';mobile.innerHTML=PAGES.slice(0,6).map(x=>`<a class="${x[0]===here?'active':''}" href="./${x[0]}">${icon(x[3])}<span>${x[2]}</span></a>`).join('');document.body.append(mobile);
let theme=localStorage.getItem('smartprep.theme')||'light';document.documentElement.dataset.theme=theme;document.querySelectorAll('[data-sp-theme]').forEach(b=>b.onclick=()=>{theme=theme==='light'?'dark':'light';document.documentElement.dataset.theme=theme;localStorage.setItem('smartprep.theme',theme)});document.querySelector('.sp-menu').onclick=()=>side.classList.toggle('open');document.addEventListener('click',e=>{if(innerWidth<901&&!side.contains(e.target)&&!e.target.closest('.sp-menu'))side.classList.remove('open')});
