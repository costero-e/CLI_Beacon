var id_region = document.getElementById("id_region");
var id_start = document.getElementById("id_start");

//add event listener to form 
form.addEventListener("submit", addItem);

function addItem(e) {

    // get customer name input value
    var start = document.getElementById("id_start").value;

    //get item purchased input value
    var region = document.getElementById("id_region").value;

    id_region.innerHTML = region;

    id_start.innerHTML = start;


}