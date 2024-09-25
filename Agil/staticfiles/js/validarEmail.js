function validateEmail() {
    const emailInput = document.getElementById('Email');
    const emailValue = emailInput.value;

    // Verifica se o campo de email está vazio ou não
    if (!emailValue) {
      alert('Por favor, insira um e-mail.');
      return false; // Evita o envio do formulário
    }

    // Regex simples para validar o formato do e-mail
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailRegex.test(emailValue)) {
      alert('Por favor, insira um e-mail válido.');
      return false; // Evita o envio do formulário
    }

    // Se todas as validações passarem, o formulário será enviado
    return true;
  }