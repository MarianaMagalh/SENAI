/*b = random(1, 15);
i = random(16, 30);
n = random(31, 45);
g = random(46, 60);
o = random(61, 75);*/

let btn = document.getElementById("sortear");

/*
// Returns a random integer from 1 to 100:
Math.floor(Math.random() * 100) + 1;
*/

function random(min, max){
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

let b = random(1, 15);
let i = random(16, 30);
let n = random(31, 45);
let g = random(46, 60);
let o = random(61, 75);

console.log("b"+b, "i"+i, "n"+n, "g"+g, "o"+o);

btn.addEventListener("click", () =>{
    // quando apertar tem que mostrar o número no div numAleatorio
});

// criar uma função para guardar o número de mostrar na 
// cartela
// acabar o bingo quando a cartela ficar completa
   
