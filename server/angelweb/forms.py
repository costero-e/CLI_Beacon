from django import forms
from django.forms import TextInput

class BamForm(forms.Form):
    choices_References = [(str(x), x) for x in range(37, 39)]
    choices = [(str(x), x) for x in range(1, 23)] + [("X", "X"), ("Y", "Y"), ("MT", "MT")]
    answer_choices = [("BOOL", "BOOL"), ("COUNT", "COUNT")]
    reference = forms.MultipleChoiceField(choices=choices_References)
    chromosome = forms.ChoiceField(choices=choices)
    start = forms.IntegerField(min_value=0, max_value=99999999999, widget=TextInput(attrs={'type':'number'}))
    region = forms.IntegerField(min_value=0, max_value=99999999999, required=False, widget=TextInput(attrs={'type':'number'}))
    alt = forms.CharField(max_length=50, required=False)
    answer_type = forms.ChoiceField(choices=answer_choices)
    liftover = forms.BooleanField(required=False)
    public = forms.BooleanField(required=False)
