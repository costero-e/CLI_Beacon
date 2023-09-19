var nameField = document.getElementById('id_region');
var lastNameValue = undefined;

updateNameDisplay();

setInterval(updateNameDisplay, 100);

function updateNameDisplay() {
  var thisValue = nameField.value || "??";
  if (lastNameValue != thisValue) {
    document.getElementById('start').innerHTML = lastNameValue = thisValue;
  }
}