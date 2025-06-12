"use strict";
console.log('Hello, world!');
// Tipos primitivos Typescript // string, boolean e number
let chuveiro = `Chuveiro`;
let ligado = true;
let temperatura = 30;
const statusChuveiro = ligado ? 'ligado' : 'desligado';
chuveiro = `O ${chuveiro} está ${statusChuveiro} e a sua temperatura é de ${temperatura} graus`;
console.log(chuveiro);
//trabalhando com objetos // objetos tipados
let produto;
let meuProduto = {
    nome: "Camiseta",
    tipodeProduto: "Roupas",
    marca: "Nike",
    preco: "R$ 29,90",
    emEstoque: true,
};
console.log(meuProduto);
// Trabalhando com arrays
let frutas = ["Maçã", "Banana", "Laranja"];
let numeros = [1, 2, 3, 4, 5];
let frutaSecas = ["Nozes", "Amêndoas", "Castanhas"];
frutaSecas.push("Nozes");
console.log(frutas);
console.log(numeros);
console.log(frutaSecas);
// Trabalhando com tuplas
let pessoa = ["João", 30, true];
let pessoa2 = ["Maria", 25, false];
let contaAgua = ["Conta de Água", 1000, 246546546406546546504605];
console.log(contaAgua);
let data = new Date("2023-10-01 21:20:00");
console.log(data);
// funções
function addNumber(a, b) {
    return a + b;
    let soma = addNumber(10, 20);
    console.log(`A soma é: ${soma}`);
}
