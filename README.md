<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Vishak Chandran VP – Fullstack Developer</title>
<link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<style>
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
:root{
  --bg:#060910;--surface:#0d1117;--card:#0f1623;
  --border:#1c2333;--border2:#21262d;
  --accent:#58a6ff;--green:#3fb950;--orange:#f78166;
  --purple:#bc8cff;--yellow:#e3b341;
  --text:#e6edf3;--muted:#7d8590;--muted2:#484f58;
}
body{
  background:var(--bg);color:var(--text);
  font-family:'Fira Code',monospace;
  min-height:100vh;display:flex;
  align-items:flex-start;justify-content:center;
  padding:40px 20px 60px;
}
body::before{
  content:'';position:fixed;inset:0;
  background-image:radial-gradient(circle,rgba(88,166,255,.05) 1px,transparent 1px);
  background-size:28px 28px;pointer-events:none;z-index:0;
}
.profile{position:relative;z-index:1;width:100%;max-width:820px;animation:rise .7s cubic-bezier(.22,1,.36,1) both}
@keyframes rise{from{opacity:0;transform:translateY(24px)}to{opacity:1;transform:translateY(0)}}

/* HEADER */
.header{
  background:var(--surface);border:1px solid var(--border);
  border-radius:14px 14px 0 0;padding:32px 36px 28px;
  position:relative;overflow:hidden;
}
.header::before{
  content:'';position:absolute;top:0;left:0;right:0;height:2px;
  background:linear-gradient(90deg,var(--accent),var(--purple),var(--green));
}
.header::after{
  content:'';position:absolute;top:-60px;right:-60px;
  width:260px;height:260px;border-radius:50%;
  background:radial-gradient(circle,rgba(88,166,255,.07) 0%,transparent 70%);
  pointer-events:none;
}
.header-inner{display:flex;align-items:flex-start;gap:24px;position:relative;z-index:1}
.avatar-zone{flex-shrink:0;text-align:center}
.avatar-gif{
  width:90px;height:90px;border-radius:50%;
  border:3px solid var(--border2);object-fit:cover;display:block;
  box-shadow:0 0 0 4px rgba(88,166,255,.1);
}
.status-indicator{
  display:inline-flex;align-items:center;gap:5px;
  margin-top:8px;font-size:10px;color:var(--green);
}
.status-dot{
  width:7px;height:7px;border-radius:50%;background:var(--green);
  animation:blink 2.2s ease-in-out infinite;
}
@keyframes blink{0%,100%{opacity:1;box-shadow:0 0 0 0 rgba(63,185,80,.5)}50%{opacity:.7;box-shadow:0 0 0 6px rgba(63,185,80,0)}}
.header-info{flex:1;min-width:0}
.greeting{font-size:11px;color:var(--muted);letter-spacing:1.2px;text-transform:uppercase;margin-bottom:6px}
.greeting span{color:var(--accent)}
.name{font-size:26px;font-weight:700;color:#fff;letter-spacing:-.5px;margin-bottom:4px}
.name .at{color:var(--muted);font-weight:300}
.handle-row{display:flex;align-items:center;gap:8px;font-size:12px;color:var(--muted);margin-bottom:12px;flex-wrap:wrap}
.handle-row a{color:var(--accent);text-decoration:none}
.handle-row a:hover{text-decoration:underline}
.pill{
  display:inline-flex;align-items:center;gap:4px;
  font-size:10px;padding:2px 8px;border-radius:20px;
  font-weight:600;letter-spacing:.6px;text-transform:uppercase;border:1px solid;
}
.pill-blue{background:rgba(88,166,255,.1);color:var(--accent);border-color:rgba(88,166,255,.25)}
.pill-green{background:rgba(63,185,80,.1);color:var(--green);border-color:rgba(63,185,80,.25)}
.tagline{font-size:13px;color:var(--text);opacity:.8;margin-bottom:16px;line-height:1.7}
.meta-row{display:flex;flex-wrap:wrap;gap:16px;font-size:11px;color:var(--muted)}
.meta-item{display:flex;align-items:center;gap:5px}
.meta-item svg{opacity:.6;flex-shrink:0}
#live-clock{color:var(--accent);font-weight:600;font-variant-numeric:tabular-nums}

/* BODY */
.body{
  background:var(--surface);border:1px solid var(--border);border-top:none;
  padding:28px 36px;display:grid;grid-template-columns:1fr 1fr;gap:24px;
}
.stats-section{grid-column:1/-1}
.stats-images{display:flex;gap:12px;flex-wrap:wrap}
.stats-images img{
  border-radius:8px;border:1px solid var(--border2);
  flex:1;min-width:240px;max-width:100%;
  transition:transform .2s,box-shadow .2s;
}
.stats-images img:hover{transform:translateY(-2px);box-shadow:0 0 20px rgba(88,166,255,.15)}

.section-label{
  font-size:10px;letter-spacing:1.5px;text-transform:uppercase;
  color:var(--muted);margin-bottom:12px;
  display:flex;align-items:center;gap:8px;
}
.section-label::before{
  content:'';display:block;width:3px;height:14px;border-radius:2px;
  background:linear-gradient(var(--accent),var(--purple));
}

/* TECH STACK */
.tech-stack-icons{display:flex;flex-wrap:wrap;gap:10px;align-items:flex-start}
.tech-icon-wrap{display:flex;flex-direction:column;align-items:center;gap:5px;cursor:default}
.tech-icon-wrap img{
  width:38px;height:38px;border-radius:8px;padding:6px;
  background:var(--card);border:1px solid var(--border2);
  transition:transform .2s,border-color .2s,box-shadow .2s;display:block;
}
.tech-icon-wrap:hover img{transform:translateY(-3px);border-color:var(--accent);box-shadow:0 4px 14px rgba(88,166,255,.2)}
.tech-icon-label{font-size:9px;color:var(--muted2);transition:color .2s}
.tech-icon-wrap:hover .tech-icon-label{color:var(--muted)}

/* TERMINAL BOX */
.term-box{
  background:var(--card);border:1px solid var(--border2);
  border-radius:10px;padding:16px;
}
.term-line{font-size:11px;color:var(--muted);line-height:2;display:flex;align-items:baseline;gap:6px}
.t-prompt{color:var(--green);flex-shrink:0}
.t-cmd{color:var(--accent)}
.t-key{color:var(--purple)}
.t-str{color:var(--yellow)}
.t-bool{color:var(--green)}
.t-val{color:var(--text)}
.cursor{
  display:inline-block;width:7px;height:13px;
  background:var(--accent);border-radius:1px;
  margin-left:2px;vertical-align:middle;
  animation:blink-cur .9s step-end infinite;
}
@keyframes blink-cur{0%,100%{opacity:1}50%{opacity:0}}

/* SOCIAL */
.social-list{display:flex;flex-direction:column;gap:9px}
.social-link{
  display:flex;align-items:center;gap:12px;
  padding:10px 14px;background:var(--card);
  border:1px solid var(--border2);border-radius:8px;
  text-decoration:none;color:var(--text);font-size:12px;
  transition:border-color .2s,background .2s,transform .15s;
}
.social-link:hover{transform:translateX(4px);border-color:var(--accent);background:rgba(88,166,255,.05)}
.social-icon{
  width:28px;height:28px;border-radius:6px;
  display:flex;align-items:center;justify-content:center;flex-shrink:0;
}
.si-ig{background:linear-gradient(135deg,#f09433,#e6683c,#dc2743,#cc2366,#bc1888)}
.si-gm{background:#D14836}
.si-li{background:#0077B5}
.social-link-text{flex:1}
.social-platform{font-weight:600;display:block;font-size:11px}
.social-handle{color:var(--muted);font-size:10px}
.social-arrow{color:var(--muted2);font-size:14px;transition:color .2s}
.social-link:hover .social-arrow{color:var(--accent)}

/* FOOTER */
.footer{
  background:var(--surface);border:1px solid var(--border);
  border-top:1px solid var(--border2);border-radius:0 0 14px 14px;
  padding:14px 36px;display:flex;align-items:center;
  justify-content:space-between;font-size:10px;color:var(--muted2);
}
.footer-left{display:flex;align-items:center;gap:6px}
.fdot{color:var(--green)}

@media(max-width:620px){
  .header-inner{flex-direction:column;align-items:center;text-align:center}
  .meta-row,.handle-row{justify-content:center}
  .body{grid-template-columns:1fr;padding:20px}
  .stats-images{flex-direction:column}
  .stats-section{grid-column:1}
  .footer{flex-direction:column;gap:6px;text-align:center}
}
</style>
</head>
<body>
<div class="profile">

  <!-- ── HEADER ── -->
  <div class="header">
    <div class="header-inner">
      <div class="avatar-zone">
        <img class="avatar-gif" src="https://i.imgflip.com/65efzo.gif" alt="coding">
        <div class="status-indicator">
          <span class="status-dot"></span> Available
        </div>
      </div>
      <div class="header-info">
        <div class="greeting">👋 &nbsp;Hello, World! — <span>open to opportunities</span></div>
        <div class="name"><span class="at">@</span>vishag10</div>
        <div class="handle-row">
          Vishak Chandran VP &nbsp;·&nbsp;
          <a href="https://github.com/vishag10" target="_blank">github.com/vishag10</a>
          <span class="pill pill-blue">Fullstack</span>
          <span class="pill pill-green">● Active</span>
        </div>
        <div class="tagline">
          Building robust, scalable web applications — from pixel to server.<br>
          Passionate about clean code, great UX &amp; continuous learning.
        </div>
        <div class="meta-row">
          <span class="meta-item">
            <svg width="12" height="12" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7z"/><circle cx="12" cy="9" r="2.5"/></svg>
            Thiruvananthapuram, Kerala, India 🇮🇳
          </span>
          <span class="meta-item">
            <svg width="12" height="12" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
            <span id="live-clock">--:--:-- IST</span>
          </span>
          <span class="meta-item">
            <svg width="12" height="12" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 21V9"/></svg>
            <a href="mailto:vishagchandran10@gmail.com" style="color:var(--muted);text-decoration:none">vishagchandran10@gmail.com</a>
          </span>
        </div>
      </div>
    </div>
  </div>

  <!-- ── BODY ── -->
  <div class="body">

    <!-- Stats -->
    <div class="stats-section">
      <div class="section-label">GitHub Statistics</div>
      <div class="stats-images">
        <img src="https://github-readme-stats.vercel.app/api?username=vishag10&hide_title=false&hide_rank=false&show_icons=true&include_all_commits=true&count_private=true&disable_animations=false&theme=github_dark&locale=en&hide_border=true&bg_color=0f1623&border_radius=8" height="155" alt="GitHub Stats">
        <img src="https://github-readme-stats.vercel.app/api/top-langs?username=vishag10&locale=en&hide_title=false&layout=compact&card_width=320&langs_count=5&theme=github_dark&hide_border=true&bg_color=0f1623&border_radius=8" height="155" alt="Top Languages">
      </div>
    </div>

    <!-- Tech Stack -->
    <div>
      <div class="section-label">Tech Stack</div>
      <div class="tech-stack-icons">
        <div class="tech-icon-wrap"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/javascript/javascript-original.svg" alt="JS"><span class="tech-icon-label">JS</span></div>
        <div class="tech-icon-wrap"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/typescript/typescript-original.svg" alt="TS"><span class="tech-icon-label">TS</span></div>
        <div class="tech-icon-wrap"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/react/react-original.svg" alt="React"><span class="tech-icon-label">React</span></div>
        <div class="tech-icon-wrap"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-original.svg" alt="HTML5"><span class="tech-icon-label">HTML5</span></div>
        <div class="tech-icon-wrap"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/css3/css3-original.svg" alt="CSS3"><span class="tech-icon-label">CSS3</span></div>
        <div class="tech-icon-wrap"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" alt="Python"><span class="tech-icon-label">Python</span></div>
        <div class="tech-icon-wrap"><img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/csharp/csharp-original.svg" alt="C#"><span class="tech-icon-label">C#</span></div>
      </div>
    </div>

    <!-- Terminal / About -->
    <div>
      <div class="section-label">About Me</div>
      <div class="term-box">
        <div class="term-line"><span class="t-prompt">➜</span><span class="t-cmd">const</span><span class="t-val">&nbsp;dev&nbsp;=&nbsp;{</span></div>
        <div class="term-line" style="padding-left:16px"><span class="t-key">name:</span><span class="t-str">&nbsp;"Vishak Chandran VP"</span><span style="color:var(--muted2)">,</span></div>
        <div class="term-line" style="padding-left:16px"><span class="t-key">role:</span><span class="t-str">&nbsp;"Fullstack Developer"</span><span style="color:var(--muted2)">,</span></div>
        <div class="term-line" style="padding-left:16px"><span class="t-key">location:</span><span class="t-str">&nbsp;"India 🇮🇳"</span><span style="color:var(--muted2)">,</span></div>
        <div class="term-line" style="padding-left:16px"><span class="t-key">skills:</span><span class="t-str">&nbsp;"Web &amp; Cloud Apps"</span><span style="color:var(--muted2)">,</span></div>
        <div class="term-line" style="padding-left:16px"><span class="t-key">openToWork:</span><span class="t-bool">&nbsp;true</span></div>
        <div class="term-line"><span class="t-val">}</span><span class="cursor"></span></div>
      </div>
    </div>

    <!-- Social -->
    <div>
      <div class="section-label">Connect With Me</div>
      <div class="social-list">
        <a class="social-link" href="https://www.instagram.com/vi._shag?igsh=MTQ0cWZqaDlza2NpcA%3D%3D&utm_source=qr" target="_blank">
          <div class="social-icon si-ig">
            <svg width="15" height="15" fill="white" viewBox="0 0 24 24"><path d="M12 2.163c3.204 0 3.584.012 4.85.07 3.252.148 4.771 1.691 4.919 4.919.058 1.265.069 1.645.069 4.849 0 3.205-.012 3.584-.069 4.849-.149 3.225-1.664 4.771-4.919 4.919-1.266.058-1.644.07-4.85.07-3.204 0-3.584-.012-4.849-.07-3.26-.149-4.771-1.699-4.919-4.92-.058-1.265-.07-1.644-.07-4.849 0-3.204.013-3.583.07-4.849.149-3.227 1.664-4.771 4.919-4.919 1.266-.057 1.645-.069 4.849-.069zm0-2.163c-3.259 0-3.667.014-4.947.072-4.358.2-6.78 2.618-6.98 6.98-.059 1.281-.073 1.689-.073 4.948 0 3.259.014 3.668.072 4.948.2 4.358 2.618 6.78 6.98 6.98 1.281.058 1.689.072 4.948.072 3.259 0 3.668-.014 4.948-.072 4.354-.2 6.782-2.618 6.979-6.98.059-1.28.073-1.689.073-4.948 0-3.259-.014-3.667-.072-4.947-.196-4.354-2.617-6.78-6.979-6.98-1.281-.059-1.69-.073-4.949-.073zm0 5.838c-3.403 0-6.162 2.759-6.162 6.162s2.759 6.163 6.162 6.163 6.162-2.759 6.162-6.163c0-3.403-2.759-6.162-6.162-6.162zm0 10.162c-2.209 0-4-1.79-4-4 0-2.209 1.791-4 4-4s4 1.791 4 4c0 2.21-1.791 4-4 4zm6.406-11.845c-.796 0-1.441.645-1.441 1.44s.645 1.44 1.441 1.44c.795 0 1.439-.645 1.439-1.44s-.644-1.44-1.439-1.44z"/></svg>
          </div>
          <div class="social-link-text"><span class="social-platform">Instagram</span><span class="social-handle">@vi._shag</span></div>
          <span class="social-arrow">→</span>
        </a>
        <a class="social-link" href="mailto:vishagchandran10@gmail.com">
          <div class="social-icon si-gm">
            <svg width="15" height="15" fill="white" viewBox="0 0 24 24"><path d="M24 5.457v13.909c0 .904-.732 1.636-1.636 1.636h-3.819V11.73L12 16.64l-6.545-4.91v9.273H1.636A1.636 1.636 0 0 1 0 19.366V5.457c0-2.023 2.309-3.178 3.927-1.964L5.455 4.64 12 9.548l6.545-4.91 1.528-1.145C21.69 2.28 24 3.434 24 5.457z"/></svg>
          </div>
          <div class="social-link-text"><span class="social-platform">Gmail</span><span class="social-handle">vishagchandran10@gmail.com</span></div>
          <span class="social-arrow">→</span>
        </a>
        <a class="social-link" href="https://www.linkedin.com/in/vishakchandran-vp-3b6b49230" target="_blank">
          <div class="social-icon si-li">
            <svg width="15" height="15" fill="white" viewBox="0 0 24 24"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 0 1-2.063-2.065 2.064 2.064 0 1 1 2.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>
          </div>
          <div class="social-link-text"><span class="social-platform">LinkedIn</span><span class="social-handle">Vishak Chandran VP</span></div>
          <span class="social-arrow">→</span>
        </a>
      </div>
    </div>

  </div>

  <!-- ── FOOTER ── -->
  <div class="footer">
    <div class="footer-left"><span class="fdot">●</span> vishag10 · GitHub Profile</div>
    <span>Made with ❤️ &nbsp;|&nbsp; Fullstack Developer · India</span>
  </div>

</div>
<script>
function updateClock(){
  const ist=new Date(new Date().toLocaleString('en-US',{timeZone:'Asia/Kolkata'}));
  const h=String(ist.getHours()).padStart(2,'0');
  const m=String(ist.getMinutes()).padStart(2,'0');
  const s=String(ist.getSeconds()).padStart(2,'0');
  const el=document.getElementById('live-clock');
  if(el)el.textContent=h+':'+m+':'+s+' IST';
}
updateClock();setInterval(updateClock,1000);
</script>
</body>
</html>
