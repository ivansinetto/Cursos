res.style.textAlign = 'center'
var img = document.createElement('img')
img.setAttribute('id', 'foto')
img.setAttribute('src', 'img/apresentacao.png')
res.appendChild(img)
document.body.style.background = '#407BFF'
function verificar() {
    var data = new Date()
    var ano = data.getFullYear()
    var fano = document.getElementById('txtano')
    var res = document.getElementById('res')
    if (Number(fano.value) == 0 || Number(fano.value) > ano) {
        window.alert('[ERRO] Verifique os dados e tente novamente!')
    } else {
        var fsex = document.getElementsByName('radsex')
        var idade = ano - Number(fano.value)
        var genero = ''
        if (fsex[0].checked) {
            genero = 'Homem'
            if (idade >= 0 && idade < 4) {
                //Bebê
                img.setAttribute('src', 'img/bebemenino.png')
                document.body.style.background = '#7E57C2'
            } else if (idade >= 5 && idade < 15){
                //Criança
                img.setAttribute('src', 'img/menino.png')
                document.body.style.background = '#92E3A9'
            } else if (idade >=15 && idade < 18) {
                //Adolescente
                img.setAttribute('src', 'img/adolescentemasculino.png')
                document.body.style.background = '#FFC727'
            } else if (idade >=18 && idade < 50) {
                //Adulto
                img.setAttribute('src', 'img/homem.png')
                document.body.style.background = '#C53F3F'
            } else if (idade >=50 && idade < 120) {
                //Idoso
                img.setAttribute('src', 'img/idoso.png')
                document.body.style.background = '#90CAF9'
            } else {
                window.alert('[Erro] Selecione uma idade abaixo de 120 anos')
                img.setAttribute('src', 'img/erro.png')
                document.body.style.background = '#CC2323'
            }
        } else if (fsex[1].checked) {
            genero = 'Mulher'
            if (idade >= 0 && idade < 4) {
                //Bebê
                img.setAttribute('src', 'img/bebemenina.png')
                document.body.style.background = '#7E57C2'
            } else if (idade >= 5 && idade < 15){
                //Criança
                img.setAttribute('src', 'img/menina.png')
                document.body.style.background = '#92E3A9'
            } else if (idade >=15 && idade < 18) {
                //Adolescente
                img.setAttribute('src', 'img/adolescentefemenino.png')
                document.body.style.background = '#FFC727'
            } else if (idade >=18 && idade < 50) {
                //Adulto
                img.setAttribute('src', 'img/mulher.png')
                document.body.style.background = '#C53F3F'
            } else if (idade >=50 && idade < 120) {
                //Idoso
                img.setAttribute('src', 'img/idosa.png')
                document.body.style.background = '#90CAF9'
            } else {
                //Alerta e Erro
                window.alert('[Erro] Selecione uma idade abaixo de 120 anos')
                img.setAttribute('src', 'img/erro.png')
                document.body.style.background = '#CC2323'
            }
        }
        if (fsex[0].checked) {
            res.innerHTML = `<p>Você um ${genero} com ${idade} anos</p>`
        } else {
            res.innerHTML = `<p>Você uma ${genero} com ${idade} anos</p>`
        }
        res.appendChild(img)
    }
}