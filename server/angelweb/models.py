from django.db import models

class BamModel(models.Model):
    choices_References = [(str(x), "GRCh" + str(x)) for x in range(37, 39)]
    choices = [(str(x), x) for x in range(1, 23)] + [("X", "X"), ("Y", "Y"), ("MT", "MT")]
    reference = models.ChoiceField(choices=choices_References, help_text="<span class='hovertext' data-hover='Name of the genome to be queried'>Reference</span>", label="")
    chromosome = models.ChoiceField(choices=choices, help_text="<span class='hovertext' data-hover='Name of the chromosome to be queried'>Chromosome</span>", label="")
    start = models.IntegerField(min_value=0, max_value=99999999999, help_text="<span class='hovertext' data-hover='Position from which query will start looking at'>Start</span>", label="")
    region = models.IntegerField(min_value=0, max_value=10000, required=False, help_text="<span class='hovertext' data-hover='Length of the query in genomic variants'>Region</span>", label="")
    mutated_allele = models.CharField(max_length=50, required=False, help_text="<span class='hovertext' data-hover='Search for a specific variation that query will look for'>Mutated Allele</span>", label="")
    liftover = models.BooleanField(required=False, help_text="<span class='hovertext' data-hover='Liftover'>Liftover</span>", label="")
    public = models.BooleanField(required=False, help_text="<span class='hovertext' data-hover='Public'>Public</span>", label="")