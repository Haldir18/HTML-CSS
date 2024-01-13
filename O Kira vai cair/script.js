document.addEventListener("DOMContentLoaded", function () {
    // Função para rolar suavemente para a seção correspondente
    function scrollToSection(sectionId) {
        const section = document.getElementById(sectionId);
        window.scrollTo({
            behavior: 'smooth',
            top: section.offsetTop - document.querySelector('header').offsetHeight
        });
    }

    // Adiciona um ouvinte de eventos a cada link de navegação
    document.querySelectorAll('nav a').forEach(link => {
        link.addEventListener('click', function (e) {
            e.preventDefault();
            const sectionId = this.getAttribute('href').substring(1);
            scrollToSection(sectionId);
        });
    });
});
