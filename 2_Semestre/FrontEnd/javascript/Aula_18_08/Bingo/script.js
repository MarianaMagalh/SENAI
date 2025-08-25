let btn = document.getElementById("sortear");
let divNum = document.getElementById("numAleatorio");
let numCartela = document.getElementById("numCartela");


function random(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

btn.addEventListener("click", () => {
    // quando apertar tem que mostrar o número no div numAleatorio
    bingo = random(1, 75);

    if (bingo >= 1 && bingo <= 15){
        document.getElementById("numAleatorio").innerHTML = "B" + bingo;
        document.getElementById("numCartela").innerHTML = "B" + bingo;
        console.log("B"+bingo);
    } else if (bingo >= 16 && bingo <= 30){
        document.getElementById("numAleatorio").innerHTML = "I" + bingo;
        document.getElementById("numCartela").innerHTML = "I" + bingo;
        console.log("I"+bingo);
    } else if (bingo >= 31 && bingo <= 45){
        document.getElementById("numAleatorio").innerHTML = "N" + bingo;
        document.getElementById("numCartela").innerHTML = "N" + bingo;
        console.log("N"+bingo);
    } else if (bingo >= 46 && bingo <= 60){
        document.getElementById("numAleatorio").innerHTML = "G" + bingo;
        document.getElementById("numCartela").innerHTML = "G" + bingo;
        console.log("G"+bingo);
    } else if (bingo >= 61 && bingo <= 75){
        document.getElementById("numAleatorio").innerHTML = "O" + bingo;
        document.getElementById("numCartela").innerHTML = "O" + bingo;
        console.log("O"+bingo);
    } else{
        alert("DEU ERRADO HAHAHHAAAAAAAAAAHA");
    }
});





