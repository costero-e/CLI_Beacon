function saving() {
var input = document.getElementById("id_region");
input.replace('[','')
input.replace("'",'')
let b = parseInt(input);
console.log(b)
localStorage.setItem("id_region", b.val());}