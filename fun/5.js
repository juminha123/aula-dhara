const prompt = require("prompt-sync")();

let opcao;
let produto = [];

for(let i = 0; i<3, i++);

console.log("menu");
console.log("1 - mostrar produtos")
console.log("2 - adicionar novo produtos")
opcao = Number(prompt("informe a opcao: "))

function mostrarProdutos(){
    for(let i = 0; i<produto.length; i++){
        console.log(produto[i])
    }

}
function adicionarProdutos(){
    produto.push(prompt("informe um novo produto: "))

}
if(opcao === 1){
   mostrarProdutos()
}
else if(opcao === 2){
    adicionarProdutos()
}