let btn = document.querySelector("button");

// aletorizar números
function random(num){
    return Math.floor(Math.random() * (num + 1));
}

btn.onclick = function(){
    let cor = 
    "rgb(" + random(255) + ", " + random(255) + ", " + random(255) + ")";

    document.body.style.backgroundColor = cor;
};