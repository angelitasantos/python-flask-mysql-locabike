$(function () {
    $("#tab-dados1").show();
    $("#tab-dados2").hide();
    $("#tab-dados3").hide();
});

function openNavTab1() {
    $("#tab-dados1").show();
    $("#tab-dados2").hide();
    $("#tab-dados3").hide();
}

function openNavTab2() {
    $("#tab-dados1").hide();
    $("#tab-dados2").show();
    $("#tab-dados3").hide();
}

function openNavTab3() {
    $("#tab-dados1").hide();
    $("#tab-dados2").hide();
    $("#tab-dados3").show();
}
