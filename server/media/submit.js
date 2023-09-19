var nameField = document.getElementById('id_region');
nameField.onkeydown = updateNameDisplay;
nameField.onkeyup = updateNameDisplay;
nameField.onkeypress = updateNameDisplay;
function updateNameDisplay() {
    document.getElementById('id_region').innerHTML = this.value || "??";
}