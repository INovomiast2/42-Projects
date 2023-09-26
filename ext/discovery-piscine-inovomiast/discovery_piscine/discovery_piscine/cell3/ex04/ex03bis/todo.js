// Todo JS (With JQuery). By INovomiast

$('#chore-input').on('keypress', function(e) {
    if(e.which == 13) {
        if($('#chore-input').val() == "") {
            alert("The Input can't be EMPTY!!");
        } else {
            const chore_template = `
                <tr>
                    <th>
                        <label>
                            <input type="checkbox" class="checkbox" />
                        </label>
                    </th>
                    <td>
                        <div class="flex items-center space-x-3">
                            <div>
                                <div class="font-bold" id="chore-title">${$('#chore-input').val()}</div>
                            </div>
                        </div>
                    </td>
                </tr>
            `;
            $('#default-chore').remove()
            $('#todo-body').append(chore_template);
            $('#chore-input').val("");
        }
    }
});

$('#clear-btn').click(function () {
    window.location.reload();
});