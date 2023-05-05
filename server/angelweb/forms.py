from django import forms

class BamForm(forms.Form):
    choices_References = [(str(x), "GRCh" + str(x)) for x in range(37, 39)]
    choices = [(str(x), x) for x in range(1, 23)] + [("X", "X"), ("Y", "Y"), ("MT", "MT")]
    answer_choices = [("BOOL", "BOOL"), ("COUNT", "COUNT")]
    reference = forms.ChoiceField(choices=choices_References)
    chromosome = forms.ChoiceField(choices=choices)
    start = forms.IntegerField(min_value=0, max_value=99999999999)
    region = forms.IntegerField(min_value=0, max_value=10000, required=False)
    mutated_allele = forms.CharField(max_length=50, required=False)
    answer_type = forms.ChoiceField(choices=answer_choices)
    liftover = forms.BooleanField(required=False)
    public = forms.BooleanField(required=False)

class BamFormTrue(forms.Form):
    def __init__(self, *args, **kwargs):
        super(BamFormTrue, self).__init__(*args, **kwargs)
        # assign a (computed, I assume) default value to the choice field
        self.initial['reference'] = '38'
    choices_References = [(str(x), "GRCh" + str(x)) for x in range(37, 39)]
    choices = [(str(x), x) for x in range(1, 23)] + [("X", "X"), ("Y", "Y"), ("MT", "MT")]
    answer_choices = [("BOOL", "BOOL"), ("COUNT", "COUNT")]
    reference = forms.ChoiceField(choices=choices_References)
    chromosome = forms.ChoiceField(choices=choices, initial='1')
    start = forms.IntegerField(min_value=0, max_value=99999999999, initial=2009986)
    region = forms.IntegerField(min_value=0, max_value=10000, required=False)
    mutated_allele = forms.CharField(max_length=50, required=False)
    answer_type = forms.ChoiceField(choices=answer_choices, initial='BOOL')
    liftover = forms.BooleanField(required=False)
    public = forms.BooleanField(required=False)


class BamFormFalse(forms.Form):
    def __init__(self, *args, **kwargs):
        super(BamFormFalse, self).__init__(*args, **kwargs)
        # assign a (computed, I assume) default value to the choice field
        self.initial['reference'] = '37'
    choices_References = [(str(x), "GRCh" + str(x)) for x in range(37, 39)]
    choices = [(str(x), x) for x in range(1, 23)] + [("X", "X"), ("Y", "Y"), ("MT", "MT")]
    answer_choices = [("BOOL", "BOOL"), ("COUNT", "COUNT")]
    reference = forms.ChoiceField(choices=choices_References)
    chromosome = forms.ChoiceField(choices=choices, initial='1')
    start = forms.IntegerField(min_value=0, max_value=99999999999, initial=7172171)
    region = forms.IntegerField(min_value=0, max_value=10000, required=False)
    mutated_allele = forms.CharField(max_length=50, required=False)
    answer_type = forms.ChoiceField(choices=answer_choices, initial='BOOL')
    liftover = forms.BooleanField(required=False)
    public = forms.BooleanField(required=False)