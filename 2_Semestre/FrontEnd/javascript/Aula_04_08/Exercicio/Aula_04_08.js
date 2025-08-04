// Exercícios feitos durante a aula de JavaScript

// exer 1
let nome = prompt("Digite o seu nome: ");

alert("Olá" + nome + "!");

// exer 2
let diciplina = prompt("Qual a sua materia favorita?");

alert("A metetéria " + diciplina + " realmente é ótima!");

// exer 3
let dataAtual = prompt("Que dia é hoje?")
console.log("Hoje é " + dataAtual + "!");

// exer 4
let duvida = confirm("Você esta preparado para o segundo semestre do SENAI?");
console.log(duvida);


// exer 5
let n1 = Number(prompt("Digite um número: "));
let n2 = Number(prompt("Digite outro número: "));

let soma = n1 + n2;
let sub = n1 - n2;
let mult = n1 * n2;
let div = n1 / n2;

alert("O resultado das operações: \nSoma: " + soma + "\nSubtração: " + sub + "\nMultiplicação: " + mult + "\nDivisão: " + div);

// exer 6
let nota1 = Number(prompt("Insira a primeira nota: "));
let nota2 = Number(prompt("Insira a segunda nota: "));
let nota3 = Number(prompt("Insira a terceira nota: "));

let media = (nota1 + nota2 + nota3) / 3;    

alert("A média do aluno é : "+ media);

// exer 7
let largura = Number(prompt("Digite a largura da parede: "));
let altura = Number(prompt("Digite a altura da parede: "));

let parede = largura * altura;

alert("A área da parede é: " + parede + "m²");

if (parede >= 2){
    let tinta = Math.ceil(parede / 2);
    alert("Você precisará de " + tinta + " lata(s) de tinta para pintar a parede.");
}else{
    alert("A área da parede é muito pequena, é necessário apenas uma lata de tinta.");
}