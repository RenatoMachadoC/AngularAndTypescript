const player1 = {

    nome: "Mário",

    valocidade: 4,

    manobralidade: 3,

    poder: 4,

    pontos: 0,

}

const player2 ={

    nome: "Brower",

    velocidade: 5,

    manobralidade: 2,

    poder: 5,

    pontos: 0,

}

 async function rollDIce() {

    return Math.floor(Math.random() * 6) + 1;

}

(async function main() {

    console.log("Iniciando a Corrida...");

})();

main();