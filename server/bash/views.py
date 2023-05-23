from django.shortcuts import render
from django.views.generic import TemplateView
import subprocess
from angelweb.forms import BamForm, BamFormTrue, BamFormFalse
import time

def return_string(value1, value2, value3, value4, value5, value6, value7, value8):
    if isinstance(value1, list):
        for value in value1:
            value1 = str(value)
            value1 = "'" + value1 + "'"
    elif isinstance(value1, int):
        value = str(value)
        value1 = value
        value1 = "'" + value1 + "'"
    else:
        value1 = str(value1)
        value1 = "'" + value1 + "'"
    if isinstance(value2, list):
        for value in value2:
            value2 = str(value)
            value2 = "'" + value2 + "'"
    elif isinstance(value2, int):
        value = str(value)
        value2 = value
        value2 = "'" + value2 + "'"
    else:
        value2 = str(value2)
        value2 = "'" + value2 + "'"
    if isinstance(value3, list):
        for value in value3:
            value3 = str(value)
            value3 = "'" + value3 + "'"
    elif isinstance(value3, int):
        value = str(value3)
        value3 = value
        value3 = "'" + value3 + "'"
    else:
        value3 = str(value3)
        value3 = "'" + value3 + "'"
    if isinstance(value4, list):
        for value in value4:
            value4 = str(value)
            value4 = "'" + value4 + "'"
    elif isinstance(value4, int):
        value = str(value4)
        value4 = value
        value4 = "'" + value4 + "'"
    elif value4 == None:
        value4 = ''
        value4 = "'" + value4 + "'"
    if isinstance(value5, list):
        for value in value5:
            value5 = str(value)
            value5 = "'" + value5 + "'"
    elif isinstance(value5, int):
        value = str(value)
        value5 = value
        value5 = "'" + value5 + "'"
    else:
        value5 = str(value5)
        value5 = "'" + value5 + "'"
    if isinstance(value7, list):
        for value in value7:
            value7 = str(value)
            value7 = "'" + value7 + "'"
    elif isinstance(value7, int):
        value = str(value)
        value7 = value
        value7 = "'" + value7 + "'"
    else:
        value7 = str(value7)
        value7 = "'" + value7 + "'"
    if value6 == True:
        value6 = 'LIFTOVER'
        value6 = "'" + value6 + "'"
    elif value6 == False:
        value6 = ''
        value6 = "'" + value6 + "'"
    if value8 == True:
        value8 = 'PUBLIC'
        value8 = "'" + value8 + "'"
    elif value8 == False:
        value8 = ''
        value8 = "'" + value8 + "'"

        
    string = value1 + ' ' + value2 + ' ' + value3+ ' ' + value4 + ' ' + value5 + ' ' + value7 + ' ' + value6 + ' ' + value8


    return string

def return_bash(value1, value2, value3, value4, value5, value6, value7, value8):
    if isinstance(value1, list):
        for value in value1:
            value1 = str(value)
            value1 = "'" + value1 + "'"
    elif isinstance(value1, int):
        value = str(value)
        value1 = value
        value1 = "'" + value1 + "'"
    else:
        value1 = str(value1)
        value1 = "'" + value1 + "'"
    if isinstance(value2, list):
        for value in value2:
            value2 = str(value)
            value2 = "'" + value2 + "'"
    elif isinstance(value2, int):
        value = str(value)
        value2 = value
        value2 = "'" + value2 + "'"
    else:
        value2 = str(value2)
        value2 = "'" + value2 + "'"
    if isinstance(value3, list):
        for value in value3:
            value3 = str(value)
            value3 = "'" + value3 + "'"
    elif isinstance(value3, int):
        value = str(value3)
        value3 = value
        value3 = "'" + value3 + "'"
    else:
        value3 = str(value3)
        value3 = "'" + value3 + "'"
    if isinstance(value4, list):
        for value in value4:
            value4 = str(value)
            value4 = "'" + value4 + "'"
    elif isinstance(value4, int):
        value = str(value4)
        value4 = value
        value4 = "'" + value4 + "'"
    elif value4 == None:
        value4 = ''
        value4 = "'" + value4 + "'"
    if isinstance(value5, list):
        for value in value5:
            value5 = str(value)
            value5 = "'" + value5 + "'"
    elif isinstance(value5, int):
        value = str(value)
        value5 = value
        value5 = "'" + value5 + "'"
    else:
        value5 = str(value5)
        value5 = "'" + value5 + "'"
    if isinstance(value7, list):
        for value in value7:
            value7 = str(value)
            value7 = "'" + value7 + "'"
    elif isinstance(value7, int):
        value = str(value)
        value7 = value
        value7 = "'" + value7 + "'"
    else:
        value7 = str(value7)
        value7 = "'" + value7 + "'"
    if value6 == True:
        value6 = 'LIFTOVER'
        value6 = "'" + value6 + "'"
    elif value6 == False:
        value6 = ''
        value6 = "'" + value6 + "'"
    if value8 == True:
        value8 = 'PUBLIC'
        value8 = "'" + value8 + "'"
    elif value8 == False:
        value8 = ''
        value8 = "'" + value8 + "'"

    
    string = value1 + ' ' + value2 + ' ' + value3+ ' ' + value4 + ' ' + value5 + ' ' + value7 + ' ' + value6 + ' ' + value8
    
    bash_string = 'bash' + ' ' + '/beacon-BED-based/exec-MAIN.bash' + ' ' + string

    bash = subprocess.check_output([bash_string], shell=True)

    bash_list = bash.split(b'\n')

    new_bash_list=[]

    for item in bash_list:
        item = item.decode("utf-8") 
        new_bash_list.append(item)

    return new_bash_list


def bash_view(request):
    template = "home.html"
    form =BamForm()
    context = {'form': form}
    if request.method == 'POST':
        form = BamForm(request.POST)
        if form.is_valid():
            context = {
                'string': return_string(form.cleaned_data['reference'], form.cleaned_data['chromosome'], form.cleaned_data['start'], form.cleaned_data['region'], form.cleaned_data['mutated_allele'], form.cleaned_data['liftover'], form.cleaned_data['answer_type'], form.cleaned_data['public']),
                'bash_out': return_bash(form.cleaned_data['reference'], form.cleaned_data['chromosome'], form.cleaned_data['start'], form.cleaned_data['region'], form.cleaned_data['mutated_allele'], form.cleaned_data['liftover'], form.cleaned_data['answer_type'], form.cleaned_data['public']),
                'form': form

            }

            timestr = time.strftime("%Y%m%d")
            file_name = timestr
            path = '/logs/' + file_name + '.txt'
            file = open(path, 'a+')  # 'a+' mode instead of 'w' mode
            file.write(return_string(form.cleaned_data['reference'], form.cleaned_data['chromosome'], form.cleaned_data['start'], form.cleaned_data['region'], form.cleaned_data['mutated_allele'], form.cleaned_data['liftover'], form.cleaned_data['answer_type'], form.cleaned_data['public']) + ' POST' + '\n')
            file.close()

            return render(request, 'base.html', context)
        
    if request.method == 'GET':
        check = 0
        params = dict(request.GET)
        for k,v in params.items():
            if k == 'reference':
                check += 1
            if k == 'chromosome':
                check += 1
            if k == 'start':
                check += 1
            if k == 'answer_type':
                check += 1
        if check > 3:
            try:
                if params['region']:
                    pass
                else:
                    params['region']=None
            except Exception:
                params['region']=None
            try:
                if params['mutated_allele']:
                    pass
                else:
                    params['mutated_allele']=""
            except Exception:
                params['mutated_allele']=""
            try:
                if params['liftover']:
                    params['liftover']=True
                else:
                    params['liftover']=False
            except Exception:
                params['liftover']=False
            try:
                if params['public']:
                    params['public']=True
                else:
                    params['public']=False
            except Exception:
                params['public']=False

            context = {
                    'string': return_string(params['reference'], params['chromosome'], params['start'], params['region'], params['mutated_allele'], params['liftover'], params['answer_type'], params['public']),
                    'bash_out': return_bash(params['reference'], params['chromosome'], params['start'], params['region'], params['mutated_allele'], params['liftover'], params['answer_type'], params['public']),
                    'form': form


                }
            
            timestr = time.strftime("%Y%m%d")
            file_name = timestr
            path = '/logs/' + file_name + '.txt'
            file = open(path, 'a+')  # 'a+' mode instead of 'w' mode
            file.write(return_string(params['reference'], params['chromosome'], params['start'], params['region'], params['mutated_allele'], params['liftover'], params['answer_type'], params['public']) + ' GET' + '\n')
            file.close()

            return render(request, 'base.html', context)
            
    
    return render(request, template, context)

def bash_true_view(request):
    template = "home.html"
    form =BamFormTrue()
    context = {'form': form}
    if request.method == 'POST':
        form = BamFormTrue(request.POST)
        if form.is_valid():
            context = {
                'string': return_string(form.cleaned_data['reference'], form.cleaned_data['chromosome'], form.cleaned_data['start'], form.cleaned_data['region'], form.cleaned_data['mutated_allele'], form.cleaned_data['liftover'], form.cleaned_data['answer_type'], form.cleaned_data['public']),
                'bash_out': return_bash(form.cleaned_data['reference'], form.cleaned_data['chromosome'], form.cleaned_data['start'], form.cleaned_data['region'], form.cleaned_data['mutated_allele'], form.cleaned_data['liftover'], form.cleaned_data['answer_type'], form.cleaned_data['public']),
                'form': form

            }

            timestr = time.strftime("%Y%m%d")
            file_name = timestr
            path = '/logs/' + file_name + '.txt'
            file = open(path, 'a+')  # 'a+' mode instead of 'w' mode
            file.write(return_string(form.cleaned_data['reference'], form.cleaned_data['chromosome'], form.cleaned_data['start'], form.cleaned_data['region'], form.cleaned_data['mutated_allele'], form.cleaned_data['liftover'], form.cleaned_data['answer_type'], form.cleaned_data['public']) + ' POST' + '\n')
            file.close()

            return render(request, 'base.html', context)
        
    if request.method == 'GET':
        check = 0
        params = dict(request.GET)
        for k,v in params.items():
            if k == 'reference':
                check += 1
            if k == 'chromosome':
                check += 1
            if k == 'start':
                check += 1
            if k == 'answer_type':
                check += 1
        if check > 3:
            try:
                if params['region']:
                    pass
                else:
                    params['region']=None
            except Exception:
                params['region']=None
            try:
                if params['mutated_allele']:
                    pass
                else:
                    params['mutated_allele']=""
            except Exception:
                params['mutated_allele']=""
            try:
                if params['liftover']:
                    params['liftover']=True
                else:
                    params['liftover']=False
            except Exception:
                params['liftover']=False
            try:
                if params['public']:
                    params['public']=True
                else:
                    params['public']=False
            except Exception:
                params['public']=False

            context = {
                    'string': return_string(params['reference'], params['chromosome'], params['start'], params['region'], params['mutated_allele'], params['liftover'], params['answer_type'], params['public']),
                    'bash_out': return_bash(params['reference'], params['chromosome'], params['start'], params['region'], params['mutated_allele'], params['liftover'], params['answer_type'], params['public']),
                    'form': form


                }
            
            timestr = time.strftime("%Y%m%d")
            file_name = timestr
            path = '/logs/' + file_name + '.txt'
            file = open(path, 'a+')  # 'a+' mode instead of 'w' mode
            file.write(return_string(params['reference'], params['chromosome'], params['start'], params['region'], params['mutated_allele'], params['liftover'], params['answer_type'], params['public']) + ' GET' + '\n')
            file.close()

            return render(request, 'base.html', context)
            
    
    return render(request, template, context)

def bash_false_view(request):
    template = "home.html"
    form =BamFormFalse()
    context = {'form': form}
    if request.method == 'POST':
        form = BamFormFalse(request.POST)
        if form.is_valid():
            context = {
                'string': return_string(form.cleaned_data['reference'], form.cleaned_data['chromosome'], form.cleaned_data['start'], form.cleaned_data['region'], form.cleaned_data['mutated_allele'], form.cleaned_data['liftover'], form.cleaned_data['answer_type'], form.cleaned_data['public']),
                'bash_out': return_bash(form.cleaned_data['reference'], form.cleaned_data['chromosome'], form.cleaned_data['start'], form.cleaned_data['region'], form.cleaned_data['mutated_allele'], form.cleaned_data['liftover'], form.cleaned_data['answer_type'], form.cleaned_data['public']),
                'form': form

            }

            timestr = time.strftime("%Y%m%d")
            file_name = timestr
            path = '/logs/' + file_name + '.txt'
            file = open(path, 'a+')  # 'a+' mode instead of 'w' mode
            file.write(return_string(form.cleaned_data['reference'], form.cleaned_data['chromosome'], form.cleaned_data['start'], form.cleaned_data['region'], form.cleaned_data['mutated_allele'], form.cleaned_data['liftover'], form.cleaned_data['answer_type'], form.cleaned_data['public']) + ' POST' + '\n')
            file.close()

            return render(request, 'base.html', context)
        
    if request.method == 'GET':
        check = 0
        params = dict(request.GET)
        for k,v in params.items():
            if k == 'reference':
                check += 1
            if k == 'chromosome':
                check += 1
            if k == 'start':
                check += 1
            if k == 'answer_type':
                check += 1
        if check > 3:
            try:
                if params['region']:
                    pass
                else:
                    params['region']=None
            except Exception:
                params['region']=None
            try:
                if params['mutated_allele']:
                    pass
                else:
                    params['mutated_allele']=""
            except Exception:
                params['mutated_allele']=""
            try:
                if params['liftover']:
                    params['liftover']=True
                else:
                    params['liftover']=False
            except Exception:
                params['liftover']=False
            try:
                if params['public']:
                    params['public']=True
                else:
                    params['public']=False
            except Exception:
                params['public']=False

            context = {
                    'string': return_string(params['reference'], params['chromosome'], params['start'], params['region'], params['mutated_allele'], params['liftover'], params['answer_type'], params['public']),
                    'bash_out': return_bash(params['reference'], params['chromosome'], params['start'], params['region'], params['mutated_allele'], params['liftover'], params['answer_type'], params['public']),
                    'form': form


                }
            
            timestr = time.strftime("%Y%m%d")
            file_name = timestr
            path = '/logs/' + file_name + '.txt'
            file = open(path, 'a+')  # 'a+' mode instead of 'w' mode
            file.write(return_string(params['reference'], params['chromosome'], params['start'], params['region'], params['mutated_allele'], params['liftover'], params['answer_type'], params['public']) + ' GET' + '\n')
            file.close()

            return render(request, 'base.html', context)
            
    
    return render(request, template, context)
# Create your views here.
