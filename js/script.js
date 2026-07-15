var themeBtn = document.getElementById("themeBtn")
var body = document.body
var form = document.getElementById("contactForm")

themeBtn.addEventListener("click",function(){
    body.classList.toggle("dark")
    boby.classList.toggle('Light')

    var isDark = body.classList.contains
    themeBtn.textContent =isDark ? "🌙 tema escuro" : "tema claro☀️😎"
})

form.addEventListener("submit", function(e){
    e.preventDefault()
})