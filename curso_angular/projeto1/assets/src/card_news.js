class Cardnews extends HTMLElement {

constructor() {

    super();
    const shadow = this.attachShadow({ mode: 'open' });
    shadow.appendChild(this.build());
    shadow.appendChild(this.styles());

}

build() {

const componentRoot = document.createElement('div');


//parte esquerda do card
const cardLeft = document.createElement('div');
cardLeft.setAttribute('class', 'card_left');

const autor = document.createElement('span');
autor.textContent = 'Autor: ' + (this.getAttribute('autor') || 'Anonimous');
// Se o atributo 'autor' não for fornecido, usa 'Autor Anonimous' como padrão

const linkTitle = document.createElement('a');
linkTitle.textContent = this.getAttribute('title') || 'No title available';
linkTitle.setAttribute('href', this.getAttribute('link') || '#');
linkTitle.textContent = 'Title: ' + linkTitle.textContent;

const newsComments = document.createElement('p');
newsComments.textContent = this.getAttribute('comments') || 'No comments available';

//parte direita do card
const cardRight = document.createElement('div');
cardRight.setAttribute('class', 'card_right');

const newsImage = document.createElement('img')
newsImage.setAttribute('src', this.getAttribute('src') || 'https://www.example.com/image.jpg');

// Appendendo os elementos criados
componentRoot.appendChild(cardLeft);
componentRoot.appendChild(cardRight);
cardLeft.appendChild(autor);
cardLeft.appendChild(linkTitle);
cardLeft.appendChild(newsComments);
cardRight.appendChild(newsImage);

return componentRoot;

}

styles() {
    const style = document.createElement('style');
    style.textContent = `
        .card {
            width: 100%;
            display: flex;
            flex-direction: row;
            box-shadow: 8px 4px 21px -4px rgba(0,0,0,0.75);
            -webkit-box-shadow: 8px 4px 21px -4px rgba(0,0,0,0.75);
            -moz-box-shadow: 8px 4px 21px -4px rgba(0,0,0,0.75);
            justify-content: space-between;
        }
        .card_left {
            display: flex;
            flex-direction: column;
            justify-content: center;
        }
        .title_news {
            margin-top: 15px;
            font-size: 30px;
        }
        .desc_news {
            color: darkgrey;
        }
        .autor_news {
            font-weight: 300;
        }
    `;
    return style;
}

}

customElements.define('card-news', Cardnews);