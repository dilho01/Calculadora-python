let display = document.getElementById('display');

function adicionarTexto(valor) {
    display.textContent += valor;
}

function limpar() {
    display.textContent = '';
}

function apagarUltimo() {
    display.textContent = display.textContent.slice(0, -1);
}

function calcular() {
    try {
        display.textContent = eval(display.textContent);
    } catch (error) {
        display.textContent = 'Erro';
    }
}
