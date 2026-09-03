const prompt = require("prompt-sync")();
function media(n1,n2,n3){
    mediaNumero = (n1,n2,n3)/3;
    return mediaNumero;
}
numero1 = Number(prompt("informe um numero: "))
numero2 = Number(prompt("informe um numero: "))
numero3 = Number(prompt("informe um numero: "))
console.log(media(numero1, numero2, numero3));