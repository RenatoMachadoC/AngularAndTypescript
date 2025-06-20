const player1 = {
    nome: "Mário",
    velocidade: 4,  // Fixed typo
    manobralidade: 3,
    poder: 4,
    pontos: 0,
};

const player2 = {
    nome: "Brower",
    velocidade: 5,
    manobralidade: 2,
    poder: 5,
    pontos: 0,
};

async function rollDice() {
    return Math.floor(Math.random() * 6) + 1;
}

async function getRoundBlock() {
    let block = Math.random();
    return block <= 0.33 ? "Pista Livre" : block <= 0.66 ? "Obstáculo" : "Confronto";
}

(async function main() {
    console.log(`Iniciando a Corrida 🚦🏁 entre ${player1.nome} e ${player2.nome}...`);

    for (let round = 1; round <= 5; round++) {
        console.log(`🏁 Rodada ${round}!`);
        let block = await getRoundBlock();
        console.log(`🚦 A rodada é: ${block}`);

        let DiceResult1 = await rollDice();
        let DiceResult2 = await rollDice();

        let TotalResult1 = 0;
        let TotalResult2 = 0;

        if (block === "Pista Livre") {
            TotalResult1 = player1.velocidade + DiceResult1;
            TotalResult2 = player2.velocidade + DiceResult2;
        } else if (block === "Obstáculo") {
            TotalResult1 = player1.manobralidade + DiceResult1;
            TotalResult2 = player2.manobralidade + DiceResult2;
        } else if (block === "Confronto") {
            let power1 = player1.poder + DiceResult1;
            let power2 = player2.poder + DiceResult2;
        }

        console.log(`Resultados da rodada: ${TotalResult1} vs ${TotalResult2}`);
    }
})();