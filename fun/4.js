const prompt = require("prompt-sync")();

function usuario(nome){
    console.log(nome);
}
let nome = prompt("informe seu nome: ");
usuario(nome)