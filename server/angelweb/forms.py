from django import forms

class BamForm(forms.Form):
    choices_References = [(str(x), "GRCh" + str(x)) for x in range(37, 39)]
    choices = [(str(x), x) for x in range(1, 23)] + [("X", "X"), ("Y", "Y"), ("MT", "MT")]
    answer_choices = [("BOOL", "BOOL"), ("COUNT", "COUNT")]
    reference = forms.ChoiceField(choices=choices_References)
    chromosome = forms.ChoiceField(choices=choices)
    start = forms.IntegerField(min_value=0, max_value=99999999999)
    region = forms.IntegerField(min_value=0, max_value=10000, required=False)
    alt = forms.CharField(max_length=50, required=False)
    answer_type = forms.ChoiceField(choices=answer_choices)
    liftover = forms.BooleanField(required=False)
    public = forms.BooleanField(required=False)
