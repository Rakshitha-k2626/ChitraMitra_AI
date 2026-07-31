console.log("🎬 ChitraMitra AI Loaded");

const button=document.querySelector("button");

button.addEventListener("click",()=>{

button.innerHTML="Finding Similar Movies...";

setTimeout(()=>{

button.innerHTML="Recommend Movies";

},1500);

});
