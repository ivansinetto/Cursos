function verificar() {
    const text = document.getElementById('textinput');
    const resultado = document.getElementById('resultado');
    const pais = text.value.trim().toLowerCase();

    if (pais === 'brasil') {
    resultado.innerHTML = `<P>Morando em ${pais} você é <strong>BRASILEIRO!</strong></P>`
    } else {
        resultado.innerHTML = `<p>Morando em ${pais} você é <strong>ESTRANGEIRO!</strong></p>`
    }
}