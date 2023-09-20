from django import forms

class BamForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(BamForm, self).__init__(*args, **kwargs)
        # assign a (computed, I assume) default value to the choice field
        self.initial['public'] = True

    def clean(self):
        cleaned_data = super(BamForm, self).clean()
        region = cleaned_data.get('region', None)
        mutated_allele = cleaned_data.get('mutated_allele', None)
        if mutated_allele and region!=0:
            self.add_error("mutated_allele", "not working")
            self.add_error("start", "not working")
            self.add_error("region", "not working")


    
    choices_References = [(str(x), "GRCh" + str(x)) for x in range(37, 39)]
    choices = [(str(x), x) for x in range(1, 23)] + [("X", "X"), ("Y", "Y"), ("MT", "MT")]
    reference = forms.ChoiceField(choices=choices_References, help_text="<span class='hovertext' data-hover='Name of the genome to be queried'>Reference</span>", label="")
    chromosome = forms.ChoiceField(choices=choices, help_text="<span class='hovertext' data-hover='Name of the chromosome to be queried'>Chromosome</span>", label="")
    start = forms.IntegerField(min_value=0, max_value=99999999999, help_text="<span class='hovertext' data-hover='Position from which query will start looking at'>Start</span>", label="")
    region = forms.IntegerField(min_value=0, max_value=10000, required=False, help_text="<span class='hovertext' data-hover='Length of the query in genomic variants'>Region</span>", label="")
    mutated_allele = forms.CharField(max_length=50, required=False, help_text="<span class='hovertext' data-hover='Search for a specific variation that query will look for'>Mutated Allele</span>", label="")
    liftover = forms.BooleanField(required=False, help_text="<span class='hovertext' data-hover='Liftover'>Liftover</span>", label="")
    public = forms.BooleanField(required=False, help_text="<span class='hovertext' data-hover='Public'>Public</span>", label="")

class BamFormTrue(forms.Form):
    def __init__(self, *args, **kwargs):
        super(BamFormTrue, self).__init__(*args, **kwargs)
        # assign a (computed, I assume) default value to the choice field
        self.initial['reference'] = '37'
        self.initial['public'] = True  
    choices_References = [(str(x), "GRCh" + str(x)) for x in range(37, 39)]
    choices = [(str(x), x) for x in range(1, 23)] + [("X", "X"), ("Y", "Y"), ("MT", "MT")]
    reference = forms.ChoiceField(choices=choices_References, help_text="<span class='hovertext' data-hover='Name of the genome to be queried'>Reference</span>", label="")
    chromosome = forms.ChoiceField(choices=choices, initial=[str(7),7],help_text="<span class='hovertext' data-hover='Name of the chromosome to be queried'>Chromosome</span>", label="")
    start = forms.IntegerField(min_value=0, max_value=99999999999, initial=140453136 ,help_text="<span class='hovertext' data-hover='Position from which query will start looking at'>Start</span>", label="")
    region = forms.IntegerField(min_value=0, max_value=10000, required=False,help_text="<span class='hovertext' data-hover='Length of the query in genomic variants'>Region</span>", label="")
    mutated_allele = forms.CharField(max_length=50, required=False, initial='', help_text="<span class='hovertext' data-hover='Search for a specific variation that query will look for'>Mutated Allele</span>", label="")
    liftover = forms.BooleanField(required=False, help_text="<span class='hovertext' data-hover='Liftover'>Liftover</span>", label="")
    public = forms.BooleanField(required=False, help_text="<span class='hovertext' data-hover='Public'>Public</span>", label="")


class BamFormFalse(forms.Form):
    def __init__(self, *args, **kwargs):
        super(BamFormFalse, self).__init__(*args, **kwargs)
        # assign a (computed, I assume) default value to the choice field
        self.initial['reference'] = '37'
        self.initial['public'] = True       
    choices_References = [(str(x), "GRCh" + str(x)) for x in range(37, 39)]
    choices = [(str(x), x) for x in range(1, 23)] + [("X", "X"), ("Y", "Y"), ("MT", "MT")]
    reference = forms.ChoiceField(choices=choices_References, help_text="<span class='hovertext' data-hover='Name of the genome to be queried'>Reference</span>", label="")
    chromosome = forms.ChoiceField(choices=choices, initial=[str(11),11], help_text="<span class='hovertext' data-hover='Name of the chromosome to be queried'>Chromosome</span>", label="")
    start = forms.IntegerField(min_value=0, initial=2142114,max_value=99999999999, help_text="<span class='hovertext' data-hover='Position from which query will start looking at'>Start</span>", label="")
    region = forms.IntegerField(min_value=0, max_value=10000, required=False, help_text="<span class='hovertext' data-hover='Length of the query in genomic variants'>Region</span>", label="")
    mutated_allele = forms.CharField(max_length=50, required=False, help_text="<span class='hovertext' data-hover='Search for a specific variation that query will look for'>Mutated Allele</span>", label="")
    liftover = forms.BooleanField(required=False, help_text="<span class='hovertext' data-hover='Liftover'>Liftover</span>", label="")
    public = forms.BooleanField(required=False, help_text="<span class='hovertext' data-hover='Public'>Public</span>", label="")
