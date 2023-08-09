function carregar() {
    var msg = document.getElementById('msg')
    var img = document.getElementById('imagem')
    var data = new Date()
    var hora = data.getHours()
    msg.innerHTML = `<p>Agora são ${hora} horas</p>`
    if (hora >= 0 && hora < 12) {
        //BOM DIA
        img.src = 'img/manha.png'
        document.body.style.background = '#E9B212'
    } else if (hora >= 12 && hora < 18) {
        //BOA TARDE
        img.src = 'img/tarde.png'
        document.body.style.background = '#92E3A9'
    } else {
        //BOA NOITE
        img.src = 'img/noite.png'
        document.body.style.background = '#BA68C8'
    }
}