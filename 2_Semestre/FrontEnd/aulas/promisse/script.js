// Promises
/*
Objeto nativo do JS que representa o resultado 
eventual de uma operação assíncrona.

EVENTUAL

- estados 
    - pending: A foi criada, mas ainda está aguardando
    o resultado da operação. Nada deu certo nem errado
    até o momento.

    - fulfilled: A operação terminou com sucesso e a
    Promise retornou um valor, cumprindo o que prometeu.

    - rejected: A operação falhou e a Promises foi rejeitada
    retornando um erro ou motivo da falha.

- foi criada para melhor o uso de callback

- Código Assincrono
  inicia tarefas demoradas, em segundo plano, 
  permitindo que o programa continue a rodar sem travar. 
  Quando a tarefa termina, uma função espeficica é chamada para 
  processar o resultado.




const ifood = new Promise((resolve, reject) => {
    console.log("Pedido aguardando confirmação...");

    const estado = true;
    setTimeout(() => {
        if (estado){
            resolve("Pedido sendo preparado");
        } else{
            reject("ops estamos sem queijo");
        }
    }, 5000);
});

ifood
    .then(msg => console.log("Sucesso: ", msg)) // possivel colocar um alert
    .catch(erro => console.log("Erro: ", erro))
    .finally(() => console.log("Operação finalizada!"));

*/
/* jogo de aposta, deve ter um saldo inicial */
let btnApostar = document.getElementById("btn-apostar");
let pSaldo = document.getElementById("saldo");
let bodyHTML = document.querySelector("body");

pSaldo = 100;

pSaldo.innerHTML = "Saldo" + pSaldo


btnApostar.addEventListener("click", () => {

})