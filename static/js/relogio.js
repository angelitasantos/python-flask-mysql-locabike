function relogio() {
    var data = new Date();
    var dia = data.getDate();
    var mes = data.getMonth() + 1;
    var ano = data.getFullYear();
    var horas = data.getHours();
    var minutos = data.getMinutes();
    var segundos = data.getSeconds();

    if (dia < 10) {
        dia = "0" + dia;
    }

    if (mes < 10) {
        mes = "0" + mes;
    }

    if (horas < 10) {
        horas = "0" + horas;
    }

    if (minutos < 10) {
        minutos = "0" + minutos;
    }

    if (segundos < 10) {
        segundos = "0" + segundos;
    }

    var string_data = dia + '/' + mes + '/' + ano;
    var string_hora = horas + ':' + minutos + ':' + segundos;

    document.getElementById("data-local").innerHTML = string_data + " - " + string_hora;

}

window.setInterval("relogio()", 1000);