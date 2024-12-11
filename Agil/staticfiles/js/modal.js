// Aguarda o carregamento total da página antes de executar o script
document.addEventListener("DOMContentLoaded", function () {
    /**
     * Função para abrir um modal específico
     * @param {string} modalId - ID do modal a ser exibido
     */
    const openModal = (modalId) => {
      const modal = document.getElementById(modalId);
      if (modal) modal.style.display = "block";
    };
  
    /**
     * Função para fechar um modal específico
     * @param {string} modalId - ID do modal a ser fechado
     */
    const closeModal = (modalId) => {
      const modal = document.getElementById(modalId);
      if (modal) modal.style.display = "none";
    };
  
    // Adiciona eventos de clique para abrir os modais
    const modalTriggers = {
      openContactModalBtn: "contactModal",
      openCompanyModalBtn: "companyModal",
      openServerManagementModalBtn: "serverManagementModal",
      OpenTermoDeCompromisso: "ModalTermoDeCompromisso1",
      OpenTermoECondições: "ModalTermosECondições",
    };
  
    Object.keys(modalTriggers).forEach((btnId) => {
      const btn = document.getElementById(btnId);
      if (btn) {
        btn.addEventListener("click", () => openModal(modalTriggers[btnId]));
      }
    });
  
    // Adiciona eventos de clique para fechar os modais através dos botões
    document.querySelectorAll(".close, .close2, .close3").forEach((button) => {
      button.addEventListener("click", function () {
        const modal = this.closest(".modal");
        if (modal) closeModal(modal.id);
      });
    });
  
    // Fecha o modal se o usuário clicar fora dele
    window.addEventListener("click", function (event) {
      if (event.target.classList.contains("modal")) {
        closeModal(event.target.id);
      }
    });
  });
  