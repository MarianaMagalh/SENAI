let btn = document.querySelector("button");

// aletorizar números
function random(num){
    return Math.floor(Math.random() * (num + 1));
}
/*function bgChange(){
    let cor = 
    "rgb(" + random(255) + ", " + random(255) + ", " + random(255) + ")";

    document.body.style.backgroundColor = cor;
}
*/
// removeEventListener - remove os eventos

// funcão anonima
/*btn.addEventListener("click", function(){
    let cor = 
    "rgb(" + random(255) + ", " + random(255) + ", " + random(255) + ")";

    document.body.style.backgroundColor = cor;
});*/

/*btn.onclick = function(){
    let cor = 
    "rgb(" + random(255) + ", " + random(255) + ", " + random(255) + ")";

    document.body.style.backgroundColor = cor;
};
*/

/*btn.addEventListener("click", ()=>{
    let cor = 
    "rgb(" + random(255) + ", " + random(255) + ", " + random(255) + ")";

    document.body.style.backgroundColor = cor;
});*/

/*
// muda a cor do botão 
function bgChange(event){
    let cor = 
    "rgb(" + random(255) + ", " + random(255) + ", " + random(255) + ")";

    event.target.style.backgroundColor = cor; // muda onde está vindo o evento
}

btn.addEventListener("click", bgChange);
*/