//Background JS (With JQuery). By INovomiast

var change_btn = $('#change-color');

function change_color() {
    var r = Math.floor(Math.random() * 256);
    var g = Math.floor(Math.random() * 256);
    var b = Math.floor(Math.random() * 256);

    return "rgb("+r+","+g+","+b+")";
}

$(change_btn).click(function (
    e) {
    e.preventDefault();
    $('body').css("background-color", change_color());

    $('#color-id').text($('body').css("background-color"));

});