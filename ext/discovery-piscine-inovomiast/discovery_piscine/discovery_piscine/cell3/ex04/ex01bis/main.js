//Ballon JS (With JQuery). By INovomiast

let count = 0;

const ballonAction = {
    'blow': (width, height) => {
        var ballonWidth = $('#ballon').width();
        var ballonHeight = $('#ballon').height();

        $('#ballon').css('width', ballonWidth+width);
        $('#ballon').css('height', ballonHeight+height);
    
        if(ballonWidth >= 300) {
            alert("The Ballon Poped!");
            window.location.reload();
        }
    },
    'switchColors': () => {
        count++;
        const colors = ['red', 'blue', 'green'];
        const bgColors = colors[count % colors.length];
        $('#ballon').css('background-color', bgColors);
    },
    'deinflate': (amount_w, amount_h) => {
        $('#ballon').css('width', amount_w);
        $('#ballon').css('height', amount_h);
        $('#ballon').css('background-color', 'red');
    }
};

$(document).ready(function () {
    $('#ballon').click(function () {
        ballonAction.blow(10, 10);
        ballonAction.switchColors();
    });
});

$('#ballon').mouseleave(function () {
    ballonAction.deinflate(200, 200);
});