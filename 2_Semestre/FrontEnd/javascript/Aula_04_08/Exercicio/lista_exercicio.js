// Lista de Exercicios de JavaScript
/*
// exer 1
let num = prompt("digite um número: ");

if (num % 2 == 0){
    console.log("par");
    if (num % 3 == 0 && num % 5 == 0){
        console.log("é divisível por 3 e 5");
        alert("O número " + num + " é par e divisível por 3 e 5.");
    }else{
        alert("O número " + num + " é par, mas não é divisível por 3 e 5.");
    }
}else{
    console.log("ímpar");
    if (num % 3 == 0 && num % 5 == 0){
        console.log("é divisível por 3 e 5");
        alert("O número " + num + " é ímpar e divisível por 3 e 5.");
    }else{
        alert("O número " + num + " é ímpar, mas não é divisível por 3 e 5.");
    }
}


// exer 2
let n1 = Number(prompt("Digite um número: "));
let n2 = Number(prompt("Digite outro número: "));
let n3 = Number(prompt("Digite mais um número: "));

let maior = Math.max(n1, n2, n3);

alert("O maior número é: " + maior);


// exer 3
let idade = Number(prompt("Digite sua idade: "));

if (idade <= 2){
    alert("Você é um bebê.");
} else if (idade <= 12){
    alert("Você é uma criança.");
} else if (idade <= 19){
    alert("Você é adolescente.");
} else if (idade <= 59){
    alert("Você é um adulto.");
} else {
    alert("Você é um idoso.");
}


// exer 4
let op = prompt('Você deseja calcular de Celcius para Fahrenheit (C) ou de Fahrenheit para Celsius (F)? ');

switch (op.toUpperCase()){
    case 'C':
        let celcius = Number(prompt("Digite a temperatura em Celsius: "));
        let fah = (celcius * 9/5) + 32;
        alert("A temperatura em Fahrenheit é: " + fah);
        break;
    case 'F':
        let fahre = Number(prompt("Digite a temperatura em Fahrenheit: "));
        let cel = (fahre - 32) * 5/9;
        alert("A temperatura em Celsius é: " + cel);            
        break;
    default:
        alert("Opção inválida. Por favor, escolha 'C' ou 'F'.");
        break;  
}


// exer 5
let valocidade = Number(prompt("Digite a velocidade do carro: "));

if (isNaN(valocidade) || valocidade < 0) {
    alert("Por favor, insira um valor válido para a velocidade.");
}
if (valocidade > 80){
    let multa = (valocidade - 80) * 5;
    alert("Você foi multado! O valor da multa é: R$ " + multa);
} else{
    alert("Você está dentro do limite de velocidade.");
}


// exer 6
let distancia = Number(prompt("Digite a distância que vc deseja percorrer em km: "));

if (distancia <= 200){
    let preco = distancia * 0.50;
    alert("O preço da passagem é R$ "+ preco.toFixed(2));
} else if (distancia > 200){
    let preco = distancia * 0.45;
    alert("O preço da passagem é R$ "+ preco.toFixed(2));
} else{
    alert("Por favor, insira uma distância válida.");
}


// exer 7
let anoNascimento = Number(prompt("Insira o seu ano de nascimento: "));

let conta = anoNascimento - 2025;

if (conta <= 18){
    alert("Você ainda não pode votar.");
} else if (conta > 18 && conta <= 70){
    alert("Você deve votar.");
} else{
    alert("Você não precisa mais votar.");
}


// exer 8 
let ano = Number(prompt("Digite um ano: "));

if ((ano % 4 === 0 && ano % 100 !== 0) || (ano % 400 === 0)) {
    alert(ano + " é um ano bissexto.");
}else {
    alert(ano + " não é um ano bissexto.");
}   

*/