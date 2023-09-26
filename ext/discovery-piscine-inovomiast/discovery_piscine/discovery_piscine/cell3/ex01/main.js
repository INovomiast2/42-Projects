// Element:Ballon(DIV)
const ballon = document.getElementById('ballon');
const bpops = document.getElementById('bpops');
const pops = document.getElementById('number-of-pops');

// Varibles for Width, Height and the max times to click before the ballon "Explodes".
let currentWidth = ballon.offsetWidth; // Takes the current ballon Width.
let currentHeight = ballon.offsetHeight; // Takes the current ballon Height.

let defaultWidthHeight = 200; // The original Width and Height of the ballon.
let max_times = 10; // The ammount of times the ballon need's to be clicked to POP.

//Local Storage: To save the amount of POP's of the ballon.
let aPops = localStorage.getItem("amountOfPops");

// On Load Page take the aPOP's from the local storage and setting it to the counter.
document.body.onload = () => {
    if(!aPops) {
        localStorage.setItem("amountOfPops", 0);
    }
    pops.innerHTML = aPops;
    console.log("Width: " + ballon.offsetWidth + "\n" + "Height: " + ballon.offsetHeight)
}


// Function: popBallon, makes the ballon to pop when it reaches a limit
function popBallon() {
    ballon.remove();
    bpops.innerHTML = "The ballon Popped! <br /> <center><button style='text-align:center; width: 300px; height: 60px; background-color:royalblue; margin-top:50px; border-radius:5px; color:white; font-size:25px; cursor:pointer;' onClick='window.location.reload()' >Inflate a New Ballon</button><center>";
    let pops = Number(aPops)+1;
    localStorage.setItem("amountOfPops", pops);
}


// Function: blowBallon, increases by the number of pixels passed thru the params.
function blowBallon(width, height) {
    currentWidth = currentWidth + width;
    currentHeight = currentHeight + height;
    ballon.style.width = currentWidth + 'px';
    ballon.style.height = currentHeight + 'px';

    if(ballon.offsetHeight && ballon.offsetWidth >= 420) {
        popBallon();
    }
}

let count = 0;

// An array of colors for cycling over them.
const colors = ['red', 'blue', 'green']

// Event that track's if the ballon was clicked and runs the function: blowBallon(), having 2 params: Width and Height changed.
ballon.addEventListener('click', () => {
    blowBallon(10, 10);
    count++
    const bgColors = colors[count % colors.length];
    ballon.style.backgroundColor = bgColors;
});

// Event that track's if the mouse leaved the ballon and returns the ballon to it's default state.
ballon.addEventListener('mouseleave', () => {
    if(ballon.style.width != defaultWidthHeight) {
        ballon.style.width = defaultWidthHeight + 'px';
        ballon.style.height = defaultWidthHeight + 'px';
        currentWidth = defaultWidthHeight;
        currentHeight = defaultWidthHeight;
        ballon.style.backgroundColor = 'red';
    } else if(ballon.style.width == defaultWidthHeight) {
        //pass
    }
});