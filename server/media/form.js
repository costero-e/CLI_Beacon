
element = document.getElementById('id_region');
if (element != null) {
if (document.getElementById('id_region').value == '1'){
      document.getElementById('id_mutated_allele').readOnly=true;
 }
   else { 
    document.getElementById('id_mutated_allele').readOnly=false;
}
}
