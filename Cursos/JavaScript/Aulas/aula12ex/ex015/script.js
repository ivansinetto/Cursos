res.style.textAlign = 'center'
var img = document.createElement('img')
img.setAttribute('id', 'foto')
img.setAttribute('src', 'img/apresentacao.png')
res.appendChild(img)
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
            } else if (idade >= 5 && idade < 15){
                //Criança
                img.setAttribute('src', 'img/menino.png')
            } else if (idade >=15 && idade < 18) {
                //Adolescente
                img.setAttribute('src', 'img/adolescentemasculino.png')
            } else if (idade >=18 && idade < 50) {
                //Adulto
                img.setAttribute('src', 'img/homem.png')
            } else if (idade >=50 && idade < 120) {
                //Idoso
                img.setAttribute('src', 'img/idoso.png')
            } else {
                window.alert('[Erro] Selecione uma idade abaixo de 120 anos')
                img.setAttribute('src', 'img/erro.png')
            }
        } else if (fsex[1].checked) {
            genero = 'Mulher'
            if (idade >= 0 && idade < 4) {
                //Bebê
                img.setAttribute('src', 'img/bebemenina.png')
            } else if (idade >= 5 && idade < 15){
                //Criança
                img.setAttribute('src', 'img/menina.png')
            } else if (idade >=15 && idade < 18) {
                //Adolescente
                img.setAttribute('src', 'img/adolescentefemenino.png')
            } else if (idade >=18 && idade < 50) {
                //Adulto
                img.setAttribute('src', 'img/mulher.png')
            } else if (idade >=50 && idade < 120) {
                //Idoso
                img.setAttribute('src', 'img/idosa.png')
            } else {
                window.alert('[Erro] Selecione uma idade abaixo de 120 anos')
                img.setAttribute('src', 'img/erro.png')
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