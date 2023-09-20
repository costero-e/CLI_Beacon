
var storedValue = localStorage.getItem("id_region");
console.log(storedValue)
storedValue.replace('[','')
storedValue.replace("'",'')
let b = parseInt(storedValue);

window.onload = function(){
  document.getElementById("id_region").value = b;
}