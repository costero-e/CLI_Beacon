var nameInput = document.getElementById('id_start');

document.querySelector('form.superform').addEventListener('submit', function (e) {

    //prevent the normal submission of the form
    e.preventDefault();

    console.log(nameInput.value);    
});