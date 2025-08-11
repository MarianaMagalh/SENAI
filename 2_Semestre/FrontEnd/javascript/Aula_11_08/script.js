// Loop´s
// 3 condições - contador, condição de saída e iterador

// for
// for (incialização; condição-saída; expressão-final) {
//     // bloco de código
// }

let cats = ["laranja", "malhado", "preto e branco"];
let info = "cores de gatinhos: ";
let i = 0;
/* 
for (let i = 0; i < cats.length; i++) {
    info += cats[i] + ", ";
}

console.log(info);


// while
// while (condição) {
//     // espressão  final
// }



while ( i < cats.length){
    if ( i == cats.length - 1){
        info += "and" + cats[i] + ".";
    } else{
        info += cats[i] + ", ";
    }
    i++;
}

console.log(info);
*/

// do while
/*
do {
    // codigo
} while (condição);


do {
    if (i === cats.length - 1){
        info += "and" + cats[i] + ".";
    } else{
        info += cats[i] + ", ";
    }
    i++;
}while (i < cats.length);

console.log(info);


// Função - em JS, uma função é um bloco de código reutilizável que pode ser executado quando chamado.
// para usar uma função, devemos fazer a declaração dela, com a seguinte sintaxe.

// function name(){}

function hi(){
    alert("OLAAAAAAAA");
}

hi();

// Funcões Anonimas - são funções que não recebe nomes, que são executadas no momento da excução, e que não será chamada em outra parte do aplicativo
// normalmente são declaradas junto á uma variável.

let soma = function(n1, n2){
    return n1 + n2;
}

alert(soma(2,3));

let hellou = function(){
    console.log("Olarrrrrrrr");
}

hellou();
*/

/*
Arrow Function - em termos simples, uma arrow function é um forma concisa de escrever uma função em JS. Ela otimiza a escrita
do seu código, deixando-o mais limpa, enxuto e aumentando a legibilidade.

const divi = (n1, n2) => {
    return n1 / n2;
}

// em uma linha só
const dividir = (n1, n2) => n1 / n2;


let soma = (n1, n2) => {
    return n1 + n2
}

console.log(soma(2, 3));
*/