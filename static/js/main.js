document.addEventListener("DOMContentLoaded",()=>{
  const revealEls=document.querySelectorAll(".reveal");
  if("IntersectionObserver" in window){
    const observer=new IntersectionObserver(entries=>entries.forEach(entry=>{if(entry.isIntersecting){entry.target.classList.add("visible");observer.unobserve(entry.target)}}),{threshold:.12});
    revealEls.forEach(el=>observer.observe(el));
  }else revealEls.forEach(el=>el.classList.add("visible"));
  const counters=document.querySelectorAll("[data-count]");
  const counterObserver=new IntersectionObserver(entries=>entries.forEach(entry=>{
    if(entry.isIntersecting){const el=entry.target,target=Number(el.dataset.count);let current=0;const step=Math.max(1,Math.ceil(target/55));const timer=setInterval(()=>{current=Math.min(target,current+step);el.textContent=current;if(current>=target)clearInterval(timer)},25);counterObserver.unobserve(el)}
  }),{threshold:.5});
  counters.forEach(el=>counterObserver.observe(el));
  const launcher=document.getElementById("chatLauncher"),panel=document.getElementById("chatPanel"),close=document.getElementById("chatClose");
  const teaser=document.getElementById("chatTeaser");
  function openChat(){panel?.classList.add("open");teaser?.classList.add("hide");setTimeout(()=>input?.focus(),180)}
  function closeChat(){panel?.classList.remove("open");teaser?.classList.remove("hide")}
  launcher?.addEventListener("click",()=>panel?.classList.contains("open")?closeChat():openChat());
  document.querySelectorAll("[data-open-chat]").forEach(el=>el.addEventListener("click",openChat));
  close?.addEventListener("click",closeChat);
  document.querySelectorAll("[data-chat-prompt]").forEach(el=>el.addEventListener("click",()=>{input.value=el.dataset.chatPrompt;openChat();form?.requestSubmit()}));
  const form=document.getElementById("chatForm"),input=document.getElementById("chatInput"),messages=document.getElementById("chatMessages");
  function addMessage(text,cls){const div=document.createElement("div");div.className=cls;div.textContent=text;messages.appendChild(div);messages.scrollTop=messages.scrollHeight;return div}
  form?.addEventListener("submit",async e=>{
    e.preventDefault();const message=input.value.trim();if(!message)return;addMessage(message,"user-msg");input.value="";
    const waiting=addMessage("Thinking...","bot-msg");
    try{const response=await fetch("/chatbot/",{method:"POST",headers:{"Content-Type":"application/json","X-CSRFToken":getCookie("csrftoken")},body:JSON.stringify({message})});const data=await response.json();waiting.textContent=data.reply||"Sorry, I couldn't prepare a reply."}
    catch(err){waiting.textContent="Sorry, the assistant is temporarily unavailable. Please use our Contact page."}
  });
  function getCookie(name){let value=null;if(document.cookie){document.cookie.split(";").forEach(cookie=>{const c=cookie.trim();if(c.startsWith(name+"="))value=decodeURIComponent(c.substring(name.length+1))})}return value}
});
