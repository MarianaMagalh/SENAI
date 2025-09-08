// Expressões Regulares
/*
- O que é
Padrões de busca que descrevem um conjunto de strings. 
Elas permitem encontrar, validar ou modificar textos de 
forma programática e eficiente.

como filtro

const texto = "Yasmin gosta de Yoga e Yuri adora Youtubers"
const regex = /\bY\w*/gi;    /* 
b - inicio da palavra; 
Y - a letra que queremos; 
w - pega tudo antes dessa letra; 
g - busca todos as palavra que começam com Y; 
i - ignora miúsculas e minúsculas

const resultado = TextDecoder.match(regexp);
console.log(resultado);

- Por que usar regex
-- validação;
-- busca;
-- substituição.
 
- Como Criar (Literal x Regex)
 -- literal
    const regex = /abc/;

 -- Regex
    const regex = new RegExp("abc", "gi");

- Métodos
São fuções disponibilizadas pela linguagem para manipular
expressões regulares. Esses métodos não são a regex em si, mas sim
ferramentas para aplica-la sobre. Há duas formas principais de utiliza-los.

- Strings
 - match();
    Usado para consulta uma string
    "abc123xyz456".macth(/\d+/g);

 - matchALL();
    especificar padrões de strings
    
 - replace();
    trocar a posição das strings

 - split();
    quebra a string em partes menores

 - search().
    procura o primeiro indice da ocorrencia

- RegeXP - identifica e extrai padrões
 - test();
    teste a string dentro do padrão, sendo True ou False

 - exec().
    procura regex dentro de um string e retornar.

- Boas práticas
 - Documentação - colocar comentario;
 - evita .* - significa qualquer coisa;
 - quatificadores - quantificadores claro;
 - fazer teste.

- Exemplos


- Grupos e Recursos avançados
 - grupos
    Trata múltiplos caracteres como uma única unidade. Tendo dois tipos
    Captura - agrupa parte de uma padrão e armazena o trecho de texto para utilizar depois.

    Não Captura - agrupa um padrão para aplicar um quantificador.

 - BackReferences
    refira a um trecho de texto que já foi capturado por um grupo.
    variavel temporaria 
*/

