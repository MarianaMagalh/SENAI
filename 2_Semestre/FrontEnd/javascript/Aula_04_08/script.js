// Obrigatorio fazer a declração de variaveis. Tipagem dinamica. 
// var - global sem ser global
// let - mais comum
// const - constante, não pode ser alterada
/*
console.log("oioi");

var uma = "uma";
let duas = "duas";
const tres = 3;

// console.log - printa no terminal no broswer
console.log(uma, duas, "Flor", tres);

// alert - mostra uma mensagem na tela
alert("Bem-Vinde!")

// prompt - mostra uma mensagem e espera o usuario digitar algo
let nome = prompt("Digite seu nome:"); 
alert("Bem Vinde " + nome + "!");

// confirm - mostra uma mensagem e espera o usuario confirmar ou cancelar
let verificacao = confirm("Voce estuda no SENAI?");
console.log(verificacao);


// Array e objetos
let arr = ["maria", "joão", "pedro", "ana"];
console.log(arr[3]);

let obj = {
    nome: "Maria",
    idade: 14,
    hobbies: ["pintar", "comer", "dançar"]
}
console.log(obj.nome);
console.log(obj.hobbies[1]);

// variaveis podem se comportar com arrays
// exemplo: acessar o terceiro caracter de uma string
let nome = "João";
console.log(nome[2])

// ou usando charAt
// charAt retorna o caracter na posição especificada
console.log(nome.charAt(2));


let a = "a";
let b = "b";

console.log(a>b);
console.log(typeof(b.toString))
console.log(arr.toString());
console.log(arr.length);
console.log(nome.slice(0, 3));
console.log(nome.toLocaleLowerCase());
console.log(nome.toUpperCase());
console.log(nome.replace("ão", "a"));


let lista = "maria, joão, pedro, ana";
lista = lista.split(", "); // divide uma string por determinado caracter e transforma em um array
console.log(lista);

lista = lista.join(", "); // junta os elementos de um array em uma string, separando por um caracter especificado
console.log(lista);

// adicionar um elemento no final do array
arr.push("Luiza");
console.log(arr);

// adicionar um elemento no começo do array
arr.unshift("Carlos");
console.log(arr);

// remover o último elemento do array
arr.pop("ana");
console.log(arr);

// remover o primeiro elemento do array
arr.shift("maria");
console.log(arr);
*/

// Condicionais
// OR = || 
// AND = &&
// NOT = ! 

if (3 > 4){
    console.log("Ok");
} else if (5 > 6){
    console.log("Ok 2");
} else{
    console.log("Não ok");
}

// estrutura de decisão switch
// é usada quando temos várias condições para verificar
let amarela = prompt("Escolha uma cor: ")

switch (amarela){
    case "amarelo":
        console.log("Você gosta de " + amarela + "!");
        break;
    case "azul":
        console.log("Você gosta de " + amarela + "!");
        break;
    case "verde":
        console.log("Você gosta de " + amarela + "!");
        break;
    case "vermelho":
        console.log("Você gosta de " + amarela + "!");
        break;
    default:
        console.log("Você não gosta de nenhuma dessas cores!");
        break;
}