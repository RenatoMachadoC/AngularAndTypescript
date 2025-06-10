class TitleDinamic extends HTMLElement {

    constructor() {
        super();
        const shadow = this.attachShadow({ mode: 'open' });


        // Constrói o elemento h1 com o texto dinâmico
        const componentRoot = document.createElement('h1');
        componentRoot.textContent = this.getAttribute(`Title`);
        
        // Define o estilo do elemento h1
        const style = document.createElement('style');
        style.textContent = `
            h1 {
                color: blue;
                font-size: 24px;
                text-align: center;
            }
        `;

        // Anexa o estilo e o elemento h1 ao shadow DOM
        shadow.appendChild(style);
        shadow.appendChild(componentRoot);

        }


}

customElements.define('title-dinamic', TitleDinamic);