document.addEventListener("DOMContentLoaded", function () {
    const btnLogin = document.getElementById("btn-login");
    const btnRegister = document.getElementById("btn-register");
    const modalOverlay = document.getElementById("modal-overlay");
    const modalBody = document.getElementById("modal-body");
    const closeModal = document.getElementById("close-modal");

    // Função para abrir o modal
    function openModal() {
        modalOverlay.classList.remove("hidden");
        modalOverlay.classList.add("visible");
    }

    // Função para fechar o modal
    function closeModalFunc() {
        modalOverlay.classList.remove("visible");
        modalOverlay.classList.add("hidden");
    }

    // Exibe o formulário de Login
    btnLogin.addEventListener("click", function () {
        modalBody.innerHTML = `
            <h2>Login</h2>
            <form id="loginForm">
                <label for="email">E-mail</label>
                <input type="email" id="email" required>
                <label for="password">Senha</label>
                <input type="password" id="password" required>
                <button type="submit">Entrar</button>
            </form>
        `;
        openModal();
    });

    // Exibe o formulário de Cadastro (Novo Vendedor) sem confirmação de senha e validação extra
    btnRegister.addEventListener("click", function () {
        modalBody.innerHTML = `
            <h2>Criar Novo Vendedor</h2>
            <form id="registerForm">
                <label for="name">Nome</label>
                <input type="text" id="name" required>
                <label for="email-register">E-mail</label>
                <input type="email" id="email-register" required>
                <label for="password-register">Senha</label>
                <input type="password" id="password-register" required>
                <button type="submit">Cadastrar</button>
            </form>
        `;
        openModal();

        const registerForm = document.getElementById("registerForm");
        registerForm.addEventListener("submit", function (e) {
            e.preventDefault();
            // Lógica de cadastro sem validação extra de senha
            alert("Vendedor cadastrado com sucesso!");
            // Se necessário, envie os dados via AJAX ou submeta o formulário:
            // registerForm.submit();
        });
    });

    // Fechar o modal ao clicar no "x" ou fora do conteúdo
    closeModal.addEventListener("click", closeModalFunc);
    modalOverlay.addEventListener("click", function (e) {
        if (e.target === modalOverlay) {
            closeModalFunc();
        }
    });
});
