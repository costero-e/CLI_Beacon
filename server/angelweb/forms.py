from django import forms

class BamForm(forms.Form):
    def clean(self):
        cleaned_data = super(BamForm, self).clean()
        region = cleaned_data.get('region', None)
        mutated_allele = cleaned_data.get('mutated_allele', None)
        if mutated_allele and region!=0:
            raise forms.ValidationError("can't fill mutated allele if region is specified")
        
    choices_References = [(str(x), "GRCh" + str(x)) for x in range(37, 39)]
    choices = [(str(x), x) for x in range(1, 23)] + [("X", "X"), ("Y", "Y"), ("MT", "MT")]
    answer_choices = [("BOOL", "BOOL"), ("COUNT", "COUNT")]
    reference = forms.ChoiceField(choices=choices_References, help_text="<span class='hovertext' data-hover='Name of the genome to be queried'>Reference</span>", label="")
    chromosome = forms.ChoiceField(choices=choices, help_text="<span class='hovertext' data-hover='Name of the chromosome to be queried'>Chromosome</span>", label="")
    start = forms.IntegerField(min_value=0, max_value=99999999999, help_text="<span class='hovertext' data-hover='Position from which query will start looking at'>Start</span>", label="")
    region = forms.IntegerField(min_value=0, max_value=10000, required=False, help_text="<span class='hovertext' data-hover='Length of the query in genomic variants'>Region</span>", label="")
    mutated_allele = forms.CharField(max_length=50, required=False, help_text="<span class='hovertext' data-hover='Search for a specific variation that query will look for'>Mutated Allele</span>", label="")
    answer_type = forms.ChoiceField(choices=answer_choices, help_text="<span class='hovertext' data-hover='BOOL for a yes/no, COUNT for number of results'>Answer type</span>", label="")
    liftover = forms.BooleanField(required=False, help_text="<span class='hovertext' data-hover='Liftover'>Liftover</span>", label="")
    

class BamFormTrue(forms.Form):
    def __init__(self, *args, **kwargs):
        super(BamFormTrue, self).__init__(*args, **kwargs)
        # assign a (computed, I assume) default value to the choice field
        self.initial['reference'] = '37'
    choices_References = [(str(x), "GRCh" + str(x)) for x in range(37, 39)]
    choices = [(str(x), x) for x in range(1, 23)] + [("X", "X"), ("Y", "Y"), ("MT", "MT")]
    answer_choices = [("BOOL", "BOOL"), ("COUNT", "COUNT")]
    reference = forms.ChoiceField(choices=choices_References, help_text="<span class='hovertext' data-hover='Name of the genome to be queried'>Reference</span>", label="")
    chromosome = forms.ChoiceField(choices=choices, initial=[str(1),1],help_text="<span class='hovertext' data-hover='Name of the chromosome to be queried'>Chromosome</span>", label="")
    start = forms.IntegerField(min_value=0, max_value=99999999999, initial=13000000 ,help_text="<span class='hovertext' data-hover='Position from which query will start looking at'>Start</span>", label="")
    region = forms.IntegerField(min_value=0, max_value=10000, initial=10000, required=False,help_text="<span class='hovertext' data-hover='Length of the query in genomic variants'>Region</span>", label="")
    mutated_allele = forms.CharField(max_length=50, required=False, help_text="<span class='hovertext' data-hover='Search for a specific variation that query will look for'>Mutated Allele</span>", label="")
    answer_type = forms.ChoiceField(choices=answer_choices, help_text="<span class='hovertext' data-hover='BOOL for a yes/no, COUNT for number of results'>Answer type</span>", label="")
    liftover = forms.BooleanField(required=False, help_text="<span class='hovertext' data-hover='Liftover'>Liftover</span>", label="")


class BamFormFalse(forms.Form):
    def __init__(self, *args, **kwargs):
        super(BamFormFalse, self).__init__(*args, **kwargs)
        # assign a (computed, I assume) default value to the choice field
        self.initial['reference'] = '37'
    choices_References = [(str(x), "GRCh" + str(x)) for x in range(37, 39)]
    choices = [(str(x), x) for x in range(1, 23)] + [("X", "X"), ("Y", "Y"), ("MT", "MT")]
    answer_choices = [("BOOL", "BOOL"), ("COUNT", "COUNT")]
    reference = forms.ChoiceField(choices=choices_References, help_text="<span class='hovertext' data-hover='Name of the genome to be queried'>Reference</span>", label="")
    chromosome = forms.ChoiceField(choices=choices, initial=[str(11),11], help_text="<span class='hovertext' data-hover='Name of the chromosome to be queried'>Chromosome</span>", label="")
    start = forms.IntegerField(min_value=0, initial=2142114,max_value=99999999999, help_text="<span class='hovertext' data-hover='Position from which query will start looking at'>Start</span>", label="")
    region = forms.IntegerField(min_value=0, max_value=10000, required=False, help_text="<span class='hovertext' data-hover='Length of the query in genomic variants'>Region</span>", label="")
    mutated_allele = forms.CharField(max_length=50, required=False, help_text="<span class='hovertext' data-hover='Search for a specific variation that query will look for'>Mutated Allele</span>", label="")
    answer_type = forms.ChoiceField(choices=answer_choices, help_text="<span class='hovertext' data-hover='BOOL for a yes/no, COUNT for number of results'>Answer type</span>", label="")
    liftover = forms.BooleanField(required=False, help_text="<span class='hovertext' data-hover='Liftover'>Liftover</span>", label="")
