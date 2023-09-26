// Chores Array
const chores = [];

// Input
const chore_input = document.getElementById('chore-input');

// DEFAULT CHORE
const default_c = document.getElementById('default-chore');

// Table
const choreTable = document.getElementById('todo-body');

// Local Storage chores variable
let chLS = localStorage.getItem("chores");


// On page load
document.body.onload = () => {
    if(!chLS) {
        localStorage.setItem("chores", chores);
    }
}

chore_input.addEventListener('keydown', (e) => {
    if(e.code == "Enter") {
        if(chore_input.value != "") {
            default_c.style.display = 'none';
            const tblcnt = document.createElement('tr');
            tblcnt.innerHTML = `
                <th>
                    <label>
                        <input type="checkbox" class="checkbox" />
                    </label>
                </th>
                <td>
                    <div class="flex items-center space-x-3">
                        <div>
                            <div class="font-bold" id="chore-title">${chore_input.value}</div>
                        </div>
                    </div>
                </td>
            `;
            choreTable.appendChild(tblcnt);
            chore_input.value = "";
        } else if(chore_input.value == "") {
            alert("The input can't be EMPTY!");
        }
    }
});

for(let i = 0; i < chores.length; i++) {
    const eldiv = document.createElement('tr');
    eldiv.innerHTML = chore_display;
    choreTable.appendChild(eldiv);
}

const clear_btn = document.getElementById('clear-btn');

clear_btn.addEventListener('click', () => {
    window.location.reload();
});

// function genChore() {
//     let tarea = prompt("Titulo de la tarea:");
//     var tarea_display = document.createElement('p').innerHTML = tarea;
//     document.body.append(tarea_display);
// }