const words = ["Eficiência", "Inovação", "Tecnologia", "Qualidade", "Tempo"];

    let currentIndex = 0;
    const textContainer = document.querySelector('.text-container');

    function typeWord(word, callback) {
        let i = 0;
        const interval = setInterval(() => {
            if (i < word.length) {
                textContainer.textContent += word.charAt(i);
                i++;
            } else {
                clearInterval(interval);
                setTimeout(callback, 1000); // Pausa antes de apagar a palavra
            }
        }, 150);
    }

    function deleteWord(callback) {
        const word = textContainer.textContent;
        let i = word.length;
        const interval = setInterval(() => {
            if (i > 0) {
                textContainer.textContent = word.substring(0, i - 1);
                i--;
            } else {
                clearInterval(interval);
                callback();
            }
        }, 100);
    }

    function changeWord() {
        typeWord(words[currentIndex], () => {
            setTimeout(() => {
                deleteWord(() => {
                    currentIndex = (currentIndex + 1) % words.length;
                    changeWord();
                });
            }, 1000); // Pausa antes de iniciar a próxima palavra
        });
    }

    // Inicializa a animação
    changeWord();