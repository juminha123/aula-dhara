console.log("Carregando dados...")
contador = 0
setInterval(() =>{ // arrow function
    contador = contador + 1;
        console.log(contador)

    
}, 800)
setTimeout(() =>{
    console.log("dados carregados com sucesso")

}, 2000)
