console.log('Hello, world!');


// Tipos primitivos Typescript // string, boolean e number

let chuveiro: string = `Chuveiro`;
let ligado: boolean = true;
let temperatura: number = 30;
const statusChuveiro = ligado ? 'ligado' : 'desligado';

chuveiro = `O ${chuveiro} está ${statusChuveiro} e a sua temperatura é de ${temperatura} graus`;
console.log(chuveiro);


//trabalhando com objetos // objetos tipados

let produto: {

    nome: "Camiseta",
    tipodeProduto: "Roupas",
    marca: "Nike",
    preco: "R$ 29,90",
    emEstoque: true,

};

type produto = {

    nome: string;
    tipodeProduto: string;
    marca: string;
    preco: string;
    emEstoque: boolean;

};

let meuProduto: produto = {
    nome: "Camiseta",
    tipodeProduto: "Roupas",
    marca: "Nike",
    preco: "R$ 29,90",
    emEstoque: true,
};

console.log(meuProduto);

// Trabalhando com arrays

let frutas: string[] = ["Maçã","Banana", "Laranja"];
let numeros: number[] = [1, 2, 3, 4, 5];
let frutaSecas: Array<string> = ["Nozes", "Amêndoas", "Castanhas"];

frutaSecas.push("Nozes");

console.log(frutas);
console.log(numeros);
console.log(frutaSecas);

// Trabalhando com tuplas

let pessoa: [string, number, boolean] = ["João", 30, true];
let pessoa2: [string, number, boolean] = ["Maria", 25, false];

let contaAgua: [string, number, number] = ["Conta de Água", 1000, 246546546406546546504605];

console.log(contaAgua);


let data: Date = new Date("2023-10-01 21:20:00");

console.log(data);
 

// funções

function addNumber(a: number,b: number): number {

    return a + b;

    let soma: number = addNumber(10, 20);

    console.log(`A soma é: ${soma}`);

}  
