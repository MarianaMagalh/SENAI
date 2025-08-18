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

function random(num){
    return Math.floor(Math.random() * num) + 1;
}

// número sorteado
console.log(random(75))

btn.addEventListener("click", () =>{
    // quando apertar tem que mostrar o número no div numAleatorio
});

// criar uma função para guardar o número de mostrar na 
// cartela
// acabar o bingo quando a cartela ficar completa
   



