// Lista de Exercicios de JavaScript
/*
// exer 1
let num = Number(prompt("digite um número: "));

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

if (idade < 2){
    alert("Você é um bebê.");
} else if (idade < 12){
    alert("Você é uma criança.");
} else if (idade < 19){
    alert("Você é adolescente.");
} else if (idade < 59){
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
        alert("A temperatura em Fahrenheit é: " + fah.toFixed(2));
        break;
    case 'F':
        let fahre = Number(prompt("Digite a temperatura em Fahrenheit: "));
        let cel = (fahre - 32) * 5/9;
        alert("A temperatura em Celsius é: " + cel.toFixed(2));            
        break;
    default:
        alert("Opção inválida. Por favor, escolha 'C' ou 'F'.");
        break;  
}


// exer 5
let valocidade = Number(prompt("Digite a velocidade do carro: "));

if (isNaN(valocidade) || valocidade < 0) {
    alert("Por favor, insira um valor válido para a velocidade.");
} else if (valocidade > 80){
    let multa = (valocidade - 80) * 5;
    alert("Você foi multado! O valor da multa é: R$ " + multa.toFixed(2));
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

let idade = 2025 - anoNascimento;

if (idade < 18){
    alert("Você ainda não pode votar.");
} else if (idade > 18 && idade <= 70){
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



// exer 9
let anoNascimento = Number(prompt("Em que ano vc nasceu? "));
let idade = 2025 - anoNascimento;

if (idade < 18){
    let nAlis = 18 - idade;
    alert("Você ainda não pode realizar o alistamento militar, faltam " + nAlis + "anos para vc se alistar.");
} else if (idade === 18){
    alert("Você deve se alistar esse ano.");
} else{
    let passou = 18 - idade;
    alert("Você passou do tempo de alistamento há " + passou + "anos.");
}



// exer 10
let comeco = Number(prompt("Em que horas o jogo começou? "));
let fim = Number(prompt("Em que horas o jogo terminou? "));

let duracao;

if (comeco < fim){
    duracao = fim - comeco;
} else{
    duracao = (24 - comeco) + fim;
}

alert("O jogo durou " + duracao + " hora(s).");



// exer 11
let horasTrabalhadas = Number(prompt("Quantas horas você trabalhou este mês?"));
let valorHora = Number(prompt("Quanto você recebe por hora (sem hora extra)?"));

let mensal = 160;

if (horasTrabalhadas == mensal) {
    let salario = horasTrabalhadas * valorHora;
    alert("Você trabalhou " + mensal + " horas, e receberá R$" + salario.toFixed(2));
} else if (horasTrabalhadas > mensal) {
    let horaExtra = horasTrabalhadas - mensal;
    let valorExtra = valorHora * 1.5;

    let salarioBase = mensal * valorHora;
    let extra = horaExtra * valorExtra;

    let total = salarioBase + extra;

    alert("Você trabalhou " + horasTrabalhadas + " horas, e fez " + horaExtra + " horas extras.\nVocê irá receber R$" + total.toFixed(2) + " reais.");
} else {
    let salario = horasTrabalhadas * valorHora;
    alert("Você trabalhou menos que a jornada mensal. Você irá receber R$" + salario.toFixed(2));
}


// exer 12
let salarioFixo = Number(prompt("Quanto é o seu salario fixo? "));
let vendas = Number(prompt("Qual o valor das vendas efutuadas? "));

let comissao = 0;

iif (vendas <= 1500) {
    comissao = vendas * 0.03;
} else {
    comissao = (1500 * 0.03) + ((vendas - 1500) * 0.05);
}

let salarioTotal = salarioFixo + comissao;

alert(
    "Total de vendas: R$" + vendas.toFixed(2) +
    "\nComissão recebida: R$" + comissao.toFixed(2) +
    "\nSalário total: R$" + salarioTotal.toFixed(2)
);



// exer 13
let numConta = Number(prompt("Insira o número da sua conta: "));
let saldo = Number(prompt("Insira o valor do seu saldo: "));
let debito = Number(prompt("Quanto vc gastou no debito: "));
let credito = Number(prompt("Qunato vc gastou no crédito: "));

let saldoAtual = saldo - (debito + credito)

if (saldoAtual > 0){
    alert("Saldo Positivo");
} else{
    alert("Saldo Negativo");
}



// exer 14
let produto = prompt("Insira o nome do produto: ");
let qtdAtual = Number(prompt("Qual a quantidade atual do produto: "));
let maximo = Number(prompt("Qual a quantidade maxima em estoque: "));
let minimo = Number(prompt("Qual a quantidade minima em estoque: "));

let media = (maximo + minimo) / 2;

if (qtdAtual >= media){
    alert("Não efetuar compra");
} else{
    alert("Efetuar compra");
}

*/

// desafio
let salarioAtual = Number(prompt("Insira o valor do seu salario atualmente: "));
let genero = prompt("Você é um Homem ou uma Mulher? ").toLowerCase();
let anosEmpresa = Number(prompt("Quantos anos vc trabalha na empresa: "));


switch (genero){
    case "mulher":
        if (anosEmpresa < 15){
            let novoSalario = salarioAtual + (salarioAtual * 0.05);
            alert("Seu salario foi ajustado para R$" + novoSalario.toFixed(2) + " reais.");
        } else if (anosEmpresa >= 15 && anosEmpresa < 20){
            let novoSalario = salarioAtual + (salarioAtual * 0.12);
            alert("Seu salario foi ajustado para R$" + novoSalario.toFixed(2) + " reais.");
        } else{
            let novoSalario = salarioAtual + (salarioAtual * 0.23);
            alert("Seu salario foi ajustado para R$" + novoSalario.toFixed(2) + "reais.");
        }
        break;
    case "homem":
        if (anosEmpresa < 20){
            let novoSalario = salarioAtual + (salarioAtual * 0.05);
            alert("Seu salario foi ajustado para R$" + novoSalario.toFixed(2) + " reais.");
        } else if (anosEmpresa >= 20 && anosEmpresa < 30){
            let novoSalario = salarioAtual + (salarioAtual * 0.13);
            alert("Seu salario foi ajustado para R$" + novoSalario.toFixed(2) + " reais.");
        } else{
            let novoSalario = salarioAtual + (salarioAtual * 0.25);
            alert("Seu salario foi ajustado para R$" + novoSalario.toFixed(2) + " reais.");
        }
        break;
    default:
        alert("Gênero inválido. Digite 'Homem' ou 'Mulher'.");
        break;
}