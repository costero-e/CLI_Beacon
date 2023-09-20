function saving() {
var input7 = document.getElementById("id_liftover").value;
console.log(input7)
input6.replace('[','')
input6.replace("'",'')
console.log(input7)
localStorage.setItem("id_liftover", input7);

var input6 = document.getElementById("id_public").value;
console.log(input6)
input6.replace('[','')
input6.replace("'",'')
console.log(input6)
localStorage.setItem("id_public", input6);


var input5 = document.getElementById("id_mutated_allele").value;
console.log(input5)
input5.replace('[','')
input5.replace("'",'')
console.log(input5)
localStorage.setItem("id_mutated_allele", input5);


var input4 = document.getElementById("id_ref_gen").value;
console.log(input4)
input4.replace('[','')
input4.replace("'",'')
console.log(input4)
localStorage.setItem("id_ref_gen", input4);


var input3 = document.getElementById("id_chromosome").value;
console.log(input3)
input3.replace('[','')
input3.replace("'",'')
let d = parseInt(input3);
console.log(d)
localStorage.setItem("id_chromosome", d);

var input2 = document.getElementById("id_start").value;
console.log(input2)
input2.replace('[','')
input2.replace("'",'')
let c = parseInt(input2);
console.log(c)
localStorage.setItem("id_start", c);

var input = document.getElementById("id_region").value;
console.log(input)
input.replace('[','')
input.replace("'",'')
let b = parseInt(input);
console.log(b)
localStorage.setItem("id_region", b);}