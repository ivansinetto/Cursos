function calcular() {
    num = document.getElementById('txtn')
    n = Number(num.value)
    res = document.getElementById('res')

    res.innerHTML = ''

    if (n == 0) {
        alert('[ERRO] você não digitou um número!')
    } else {
        for(let c = 1; c <= 10; c++) {
            res.innerHTML += `${n} X ${c} = ${n*c} <br>`
        }
    }
}