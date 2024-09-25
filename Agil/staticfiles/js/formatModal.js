
  document.getElementById('identification').addEventListener('change', function() {
    var cpfField = document.getElementById('cpf');
    var cnpjField = document.getElementById('cnpj');
    var cpfLabel = document.getElementById('cpfLabel');
    var cnpjLabel = document.getElementById('cnpjLabel');

    if (this.value === 'individual') {
      cpfField.style.display = 'block';
      cnpjField.style.display = 'none';
      cpfLabel.style.display = 'block';
      cnpjLabel.style.display = 'none';
      cpfField.required = true;
      cnpjField.required = false;
    } else if (this.value === 'company') {
      cpfField.style.display = 'none';
      cnpjField.style.display = 'block';
      cpfLabel.style.display = 'none';
      cnpjLabel.style.display = 'block';
      cpfField.required = false;
      cnpjField.required = true;
    } else {
      cpfField.style.display = 'none';
      cnpjField.style.display = 'none';
      cpfLabel.style.display = 'none';
      cnpjLabel.style.display = 'none';
      cpfField.required = false;
      cnpjField.required = false;
    }
  });

  // Função para formatar CPF
  function formatCPF(cpf) {
    return cpf.replace(/\D/g, '')  // Remove todos os caracteres não numéricos
               .replace(/(\d{3})(\d)/, '$1.$2')  // Adiciona ponto
               .replace(/(\d{3})(\d)/, '$1.$2')  // Adiciona ponto
               .replace(/(\d{3})(\d{1,2})$/, '$1-$2');  // Adiciona hífen
  }

  // Função para formatar CNPJ
  function formatCNPJ(cnpj) {
    return cnpj
        .replace(/\D/g, '') // Remove todos os caracteres não numéricos
        .replace(/^(\d{2})(\d)/, '$1.$2') // Adiciona o primeiro ponto
        .replace(/\.(\d{3})(\d)/, '.$1.$2') // Adiciona o segundo ponto
        .replace(/\.(\d{3})(\d)/, '.$1/$2') // Adiciona a barra
        .replace(/(\d{4})(\d)/, '$1-$2') // Adiciona o hífen
        .slice(0, 18); // Limita o tamanho da string a 18 caracteres
}

  document.getElementById('cpf').addEventListener('input', function() {
    this.value = formatCPF(this.value);
  });

  document.getElementById('cnpj').addEventListener('input', function() {
    this.value = formatCNPJ(this.value);
});