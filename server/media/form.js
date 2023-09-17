 function makeReadOnly()
 {        
  if (document.getElementById('id_region').value != ''){
      document.getElementById('id_mutated_allele').readOnly=true;
 }else if (document.getElementById('id_region').value != '0'){ 
      document.getElementById('id_mutated_allele').readOnly=true;
  } else { 
    document.getElementById('id_mutated_allele').readOnly=false;
}
 }
 document.getElementById('id_region').addEventListener('change', makeReadOnly);
