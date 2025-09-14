// document.addEventListener("DOMContentLoaded", function () {
//     const estiloSelect = document.getElementById("estilo");
//     const opcoesExtra = document.getElementById("opcoes-extra");

//     estiloSelect.addEventListener("change", function () {
//         if (this.value === "aventureiro" || this.value === "heroico") {
//             opcoesExtra.style.display = "block"; // mostra opções
//         } else {
//             opcoesExtra.style.display = "none";  // esconde para clássico
//         }
//     });
// });

document.addEventListener("DOMContentLoaded", function () {
    const atributos = document.querySelectorAll("#atributos-lista .valor");
    const botoes = document.querySelectorAll("#valores button");
    const hiddenInput = document.getElementById("atributos-ordem");
    const enviarBtn = document.getElementById("enviar");

    let ordem = []; // lista de valores escolhidos
    let index = 0;  // qual atributo preencher

    botoes.forEach(btn => {
        btn.addEventListener("click", function () {
            const valor = this.getAttribute("data-valor");

            if (index < atributos.length) {
                atributos[index].textContent = valor; // mostra ao lado do atributo
                ordem.push(valor);                    // guarda valor na lista
                this.style.display = "none";          // esconde botão usado
                index++;
            }

            // sempre atualiza o hidden input
            hiddenInput.value = ordem.join(",");
        });
    });
});
