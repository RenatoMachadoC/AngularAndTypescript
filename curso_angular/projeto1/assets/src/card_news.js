class Cardnews extends HTMLElement {

constructor() {

    super();
    const shadow = this.attachShadow({ mode: 'open' });
    shadow.innerHTML = "CARD NEWS";

}

build() {

const componentRoot = document.createElement('div');


//parte esquerda do card
const cardLeft = document.createElement('div');
cardLeft.setAttribute('class', 'card_left');

const autor = document.createElement('span');

const linkTitle = document.createElement('a');

const newsComments = document.createElement('p');

//parte direita do card
const cardRight = document.createElement('div');
cardRight.setAttribute('class', 'card_right');

const newsImage = document.createElement('img');


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



}

}

custonmElements.define('card-news', Cardnews);