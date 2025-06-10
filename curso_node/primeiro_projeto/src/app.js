const player1 = {

    nome: "Mário",

    valocidade: 4,

    manobralidade: 3,

    poder: 4,

    pontos: 0,

}

const player2 = {

    nome: "Brower",

    velocidade: 5,

    manobralidade: 2,

    poder: 5,

    pontos: 0,

}

 async function rollDIce() {

    return Math.floor(Math.random() * 6) + 1;

}


async function playRaceEngine(caracter1, caracter2) {

    for ( let round = 1; round <= 5; round++){

        console.log(`🏁 Rodada ${round}!`)
    }

    let block = await getRoundBlock();
    console.log(`🚦 A rodada é: ${block}`);

}

async function getRoundBlock() {
    let block = Math.random();
    let resultado;

    switch (true) {
        case block <= 0.33:
            resultado = "Pista Livre";
            break;
        case block <= 0.66:
            resultado = "Obstáculo";
            break;
        default:
            resultado = "Confronto";
            break;
    }

    return resultado;
}

(async function main() {

    console.log(`Iniciando a Corrida 🚦🏁 entre ${player1.nome} e ${player2.nome}...`);


    await playRaceEngine(player1, player2);

})();