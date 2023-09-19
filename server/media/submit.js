var nameInput = document.getElementById('id_start');

document.querySelector('form.superform').addEventListener('submit', function (e) {

    var newValue = nameInput.value;
    console.log(newValue);
    document.getElementById('id_start').value = newValue;   
});

