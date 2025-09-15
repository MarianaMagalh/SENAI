/* WEB COMPONENTES

- O QUE É?
    suite de diferentes tecnologias que permite a criação de elementos customizados reutilizáveis
    Formado por 3 tecnologias princioais, que juntos, criam elementos customizados com funcionalidade 
    encaspsulada, para evitar conflito no codigo.

    - Elementos customizados
        Conjunto de Apis JS que permite definir elementos custumizados e seus comportamentos pode
        ndo ser utilizados de diferentes maneiras na interface.

    - Shadow DOM
        permite criar componenter isolados, com HTML, CSS e comportamento prórpio, sem afetar o restante da pagina.
    
    - Modelos HTML
        <tamplate> e <slot> permitem criar modelos html reutilizaveis e ocultos que servem como base para 
        elementos personalizados sem aparecer diretamente na pagina.

- POR QUE USAR?
    - Reutilização: mesmo componete em varias paginas.
    - Customização: criar elementos proprios como <meu-botao>.
    - Isolamento: estilos e scripts não se misturam.
    - Integração: funcionam com qualquer framewok ou sem nenhum.

Não usar em projetos simples
Muitos Frameworks já fazem isso
Não é compativel com todos os navegadores
*/

class OlaMundo extends HTMLElement {
    constructor() { 
        super()
    }
    
    connectedCallback(){
        this.innerHTML = "<p>Ola Mundo</p>";
    }
}

customElements.define("ola-mundo", OlaMundo)

class nome extends HTMLElement {
    constructor(){
        super()
    }

    connectedCallback(){
        this.innerHTML = "<p>Meu nome é Mariana</p>";
    }
}

customElements.define("meu-nome", nome)