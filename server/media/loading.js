
var storedValue = localStorage.getItem("id_region");
console.log(storedValue)

var storedValue2 = localStorage.getItem("id_start");
console.log(storedValue2)
storedValue2.replace('[','')
storedValue2.replace("'",'')
let c = parseInt(storedValue2);

var storedValue3 = localStorage.getItem("id_chromosome");
console.log(storedValue3)
storedValue3.replace('[','')
storedValue3.replace("'",'')
let d = parseInt(storedValue3);

var storedValue4 = localStorage.getItem("id_ref_gen");
console.log(storedValue4)
storedValue4.replace('[','')
storedValue4.replace("'",'')

var storedValue5 = localStorage.getItem("id_mutated_allele");
console.log(storedValue5)
storedValue5.replace('[','')
storedValue5.replace("'",'')

var storedValue6 = localStorage.getItem("id_public");
console.log(storedValue6)
storedValue6.replace('[','')
storedValue6.replace("'",'')

var storedValue7 = localStorage.getItem("id_liftover");
console.log(storedValue7)
storedValue7.replace('[','')
storedValue7.replace("'",'')


window.onload = function(){
  document.getElementById("id_region").value = storedValue;
  document.getElementById("id_start").value = c;
  document.getElementById("id_chromosome").value = d;
  document.getElementById("id_ref_gen").value = storedValue4;
  document.getElementById("id_mutated_allele").value = storedValue5;
  document.getElementById("id_public").value = storedValue6;
  document.getElementById("id_liftover").value = storedValue7;
}