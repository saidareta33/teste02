// Seleciona o formulário
const formulario = document.querySelector("form");

// Escuta o envio do formulário
formulario.addEventListener("submit", function(event) {

    // Impede o envio normal
    event.preventDefault();

    // Pega os valores dos inputs
    const gmail = document.querySelector('input[name="gmail"]').value;
    const senha = document.querySelector('input[name="senha"]').value;

    // Verifica se é um Gmail válido
    if(email.includes("@gmail.com") && senha.length >= 4){

        // Mensagem
        alert("Login realizado com sucesso!");

        // Redireciona para a página desejada
        window.location.href = "/painel";
        // Exemplos:
        // window.location.href = "/painel";
        // window.location.href = "home.html";

    } else {

        alert("Digite um Gmail válido!");

    }

});