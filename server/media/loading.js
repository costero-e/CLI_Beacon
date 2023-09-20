
var storedValue = localStorage.getItem("id_region");

window.onload = function(){
  document.getElementById("id_region").value = storedValue;
}