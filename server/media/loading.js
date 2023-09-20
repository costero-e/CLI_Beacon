
var storedValue = localStorage.getItem("id_region");
console.log(storedValue)

var storedValue2 = localStorage.getItem("id_start");
console.log(storedValue2)

var storedValue3 = localStorage.getItem("id_chromosome");
console.log(storedValue3)

var storedValue4 = localStorage.getItem("id_ref_gen");
console.log(storedValue4)

var storedValue5 = localStorage.getItem("id_mutated_allele");
console.log(storedValue5)

var storedValue6 = localStorage.getItem("id_public");
console.log(storedValue6)

var storedValue7 = localStorage.getItem("id_liftover");
console.log(storedValue7)


window.onload = function(){
  document.getElementById("id_region").value = storedValue;
  document.getElementById("id_start").value = storedValue2;
  document.getElementById("id_chromosome").value = storedValue3;
  document.getElementById("id_ref_gen").value = storedValue4;
  document.getElementById("id_mutated_allele").value = storedValue5;
  document.getElementById("id_public").value = storedValue6;
  document.getElementById("id_liftover").value = storedValue7;
}