from django.shortcuts import render
from django.views.generic import TemplateView
import subprocess
from angelweb.forms import BamForm

def execute_bash():
    #bash = subprocess.check_output(['cd', '/data/boxes/beacon-BED-based', '&&', 'bash', 'exec-MAIN.bash', '38', '4', '8000190', '2', "'T'", 'BOOL', 'LIFTOVER', 'PUBLIC'])
    bash = subprocess.check_output(['ls'])

    return bash

def return_bash(value1, value2, value3, value4, value5, value6, value7, value8):
    if isinstance(value1, list):
        for value in value1:
            value = str(value)
            value1 = value
    elif isinstance(value1, int):
        value = str(value)
        value1 = value
    if isinstance(value2, list):
        for value in value2:
            value = str(value)
            value2 = value
    elif isinstance(value2, int):
        value = str(value)
        value2 = value
    if isinstance(value3, list):
        for value in value3:
            value = str(value)
            value3 = value
    elif isinstance(value3, int):
        value = str(value3)
        value3 = value
    if isinstance(value4, list):
        for value in value4:
            value = str(value)
            value4 = value
    elif isinstance(value4, int):
        value = str(value4)
        value4 = value
    if isinstance(value5, list):
        for value in value5:
            value = str(value)
            value5 = value
    elif isinstance(value5, int):
        value = str(value)
        value5 = value
    if isinstance(value7, list):
        for value in value6:
            value = str(value)
            value7 = value
    elif isinstance(value7, int):
        value = str(value)
        value7 = value
    if value6 == True:
        value6 = 'LIFTOVER'
    elif value6 == False:
        value6 = ''
    if value8 == True:
        value8 = 'PUBLIC'
    elif value8 == False:
        value8 = ''

        
    string = value1 + ' ' + value2 + ' ' + value3+ ' ' + value4 + ' ' + value5 + ' ' + value7 + ' ' + value6 + ' ' + value8

    return string


def bash_view(request):
    template = "home.html"
    bash_out = execute_bash()
    form =BamForm()
    context = {'bash_out': bash_out,
               'form': form}
    
    if request.method == 'POST':
        form = BamForm(request.POST)
        if form.is_valid():
            context = {
                'start': form.cleaned_data['start'],
                'region': form.cleaned_data['region'],
                'bash_out': return_bash(form.cleaned_data['reference'], form.cleaned_data['chromosome'], form.cleaned_data['start'], form.cleaned_data['region'], form.cleaned_data['alt'], form.cleaned_data['liftover'], form.cleaned_data['answer_type'], form.cleaned_data['public'])

            }
            return render(request, 'form_response.html', context)
            
    
    return render(request, template, context)

# Create your views here.
