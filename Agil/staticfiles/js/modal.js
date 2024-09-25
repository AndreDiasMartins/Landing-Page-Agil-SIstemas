 // Função para abrir um modal específico
 function openModal(modalId) {
    var modal = document.getElementById(modalId);
    if (modal) {
        modal.style.display = "block";
    }
}

// Função para fechar um modal específico
function closeModal(modalId) {
    var modal = document.getElementById(modalId);
    if (modal) {
        modal.style.display = "none";
    }
}

// Adiciona eventos de clique aos links que abrem modais
document.getElementById("openContactModalBtn").onclick = function() {
    openModal("contactModal");
};

document.getElementById("openCompanyModalBtn").onclick = function() {
    openModal("companyModal");
};

document.getElementById("openServerManagementModalBtn").onclick = function() {
    openModal("serverManagementModal");
};


document.getElementById("OpenTermoDeCompromisso").onclick = function() {
    openModal("ModalTermoDeCompromisso1");
};

document.getElementById("OpenTermoECondições").onclick = function() {
    openModal("ModalTermosECondições");
};



// Adiciona eventos de clique aos botões de fechamento dos modais
document.querySelectorAll(".close, .close2, .close3").forEach(function(span) {
    span.onclick = function() {
        var modalId = this.closest(".modal").id;
        closeModal(modalId);
    };
});

// Fecha o modal se o usuário clicar fora dele
window.onclick = function(event) {
    if (event.target.classList.contains("modal")) {
        closeModal(event.target.id);
    }
};