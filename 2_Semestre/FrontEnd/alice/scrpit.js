// forma de fazer requisições de apis
fetch("https://csscolorsapi.com/api/colors")
    .then(res => res.json()) // se o fetch funcionar, vai transforma a respota em json
    .then(dados => {
        const lista = document.getElementById("lista") // chamando a div lista
        const cores = dados.colors || dados; // acessando a api

        cores.forEach(cor => {
            const item = document.createElement("article"); // criando um elemento para os dados da api
            item.className = "cor";

            const quadrado = document.createElement("div"); // criando uma div para as cores
            quadrado.className = "quadrado;"
            quadrado.style.backgroundColor = "#" + cor.hex; // colocando cor em hex na div

            const texto = document.createElement("h2");
            texto.textContent = `${cor.name} - #{cor.hex}` // mostrando o nome da cor e a cor 

            item.appendChild(quadrado);
            item.appendChild(texto);
            lista.appendChild(item);
        });
    })
    // caso dê erro
    .catch(err => console.error("Erro ao carregar as cores: ", err));