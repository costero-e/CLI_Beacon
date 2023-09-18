from django.shortcuts import render
from django.views.generic import TemplateView
import subprocess
from angelweb.forms import BamForm, BamFormTrue, BamFormFalse
import time
from django.http import HttpResponseRedirect, HttpResponseBadRequest
import logging

LOG = logging.getLogger(__name__)

def return_string(value1, value2, value3, value4, value5, value6, current_email):
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
    for value in value6:
        if value == 'True':
            value6 = 'LIFTOVER'
            value6 = "'" + value6 + "'"
        else:
            value6 = ''
            value6 = "'" + value6 + "'"

        
    string = ' --chr' + ' ' + value2 + ' --pos' + ' ' + value3 + ' --ref_gen' + ' ' + value1

    if current_email:
        string = string +  ' --email' + ' ' + str(current_email)
    if value6 == "'LIFTOVER'":
        string = string + ' --liftover'
    print(string)
    if value4:
        string = string + ' -w' + ' ' + value4 
    if value5:
        string = string + ' -a' + ' ' + value5

    return string

def return_list(value1, value2, value3, value4, value5, value6):
    if isinstance(value1, list):
        for value in value1:
            value1 = str(value)
    elif isinstance(value1, int):
        value = str(value)
        value1 = value
    else:
        value1 = str(value1)
    if isinstance(value2, list):
        for value in value2:
            value2 = str(value)
    elif isinstance(value2, int):
        value = str(value)
        value2 = value
    else:
        value2 = str(value2)
    if isinstance(value3, list):
        for value in value3:
            value3 = str(value)
    elif isinstance(value3, int):
        value = str(value3)
        value3 = value
    else:
        value3 = str(value3)
    if isinstance(value4, list):
        for value in value4:
            value4 = str(value)
    elif isinstance(value4, int):
        value = str(value4)
        value4 = value
    elif value4 == None:
        value4 = ''
    if isinstance(value5, list):
        for value in value5:
            value5 = str(value)
            value5 = "'" + value5 + "'"
    elif isinstance(value5, int):
        value = str(value)
        value5 = value
    else:
        value5 = str(value5)

    for value in value6:
        if value == 'True':
            value6 = 'LIFTOVER'
            value6 = "'" + value6 + "'"
        elif value == 'False':
            value6 = ''
            value6 = "'" + value6 + "'"

    string_list = []
    string_list.append(value1)
    string_list.append(value2)
    string_list.append(value3)
    string_list.append(value4)
    string_list.append(value5)
    string_list.append(value6)



    return string_list

def return_datasets(value1, value2, value3, value4, value5, value6, current_email):
    print(value1)
    LOG.debug(value1)
    print(value2)
    LOG.debug(value2)
    print(value3)
    LOG.debug(value3)
    print(value4)
    LOG.debug(value4)
    print(value5)
    LOG.debug(value5)
    print(value6)
    LOG.debug(value6)
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


    for value in value6:
        if value == 'True':
            value6 = 'LIFTOVER'
            value6 = "'" + value6 + "'"
        else:
            value6 = ''
            value6 = "'" + value6 + "'"

    string = ' --chr' + ' ' + value2 + ' --pos' + ' ' + value3 + ' --ref_gen' + ' ' + value1

    if current_email:
        string = string +  ' --email' + ' ' + str(current_email)
    if value6 == "'LIFTOVER'":
        string = string + ' --liftover'

    print(string)
    if value4 != "''":
        string = string + ' -w' + ' ' + value4 
    if value5 != "''":
        string = string + ' -a' + ' ' + value5
    
    bash_string = 'cd /beacon-BED-based/ ' + '&&' + ' python3 main.py' + string

    try:
        bash = subprocess.check_output([bash_string], shell=True)
    except subprocess.CalledProcessError as e:
        output = e.output
        print(output)

    bash_list = bash.split(b'\n')

    new_bash_list=[]
    for item in bash_list:
        item = item.decode("utf-8") 
        item = item.replace('[', '')
        item = item.replace(']', '')
        item = item.replace('(', '')
        item = item.replace(')', '')
        item = item.replace(' ', '')
        item = item.replace("'", '')
        item = item.replace('"', '')
        print("item is: {}".format(item))
        item_list = item.split(',')
        print("item_list is: {}".format(item_list))
        boolean = item_list[0]
        print("boolean: {}". format(boolean))
        num_results = item_list[1]
        end = len(item_list)
        datasets_list = item_list[2:end]

        break
    
    num_datasets = len(datasets_list)
    dataset_dict={}
    last_element=''
    for element in datasets_list:
        if last_element != element and last_element != '':
            dataset_dict[last_element]=element
            last_element=''
        else:
            last_element=element
    print("datasets_dict: {}". format(dataset_dict))

    dataset_dict["num_datasets"] = num_datasets
    dataset_dict["num_results"] = num_results
    dataset_dict["boolean"] = boolean


    

    return dataset_dict



def bash_view(request):
    template = "home.html"
    form =BamForm()
    context = {'form': form}
    if request.user.is_authenticated:
        current_email=request.user.email
        print(current_email)
        LOG.debug(current_email)
    else:
        current_email = ''
    if request.method == 'POST':
        form = BamForm(request.POST)
        
        if form.is_valid():
            if form.cleaned_data['region'] != None and form.cleaned_data['mutated_allele'] != '':
                get_string='?reference={}&chromosome={}&start={}&region={}&mutated_allele={}&liftover={}'.format(form.cleaned_data['reference'], form.cleaned_data['chromosome'], form.cleaned_data['start'], form.cleaned_data['region'], form.cleaned_data['mutated_allele'], form.cleaned_data['liftover'])
            elif form.cleaned_data['region'] != None:
                get_string='?reference={}&chromosome={}&start={}&region={}&liftover={}'.format(form.cleaned_data['reference'], form.cleaned_data['chromosome'], form.cleaned_data['start'], form.cleaned_data['region'],form.cleaned_data['liftover'])
            elif form.cleaned_data['mutated_allele'] != '':
                get_string='?reference={}&chromosome={}&start={}&mutated_allele={}&liftover={}'.format(form.cleaned_data['reference'], form.cleaned_data['chromosome'], form.cleaned_data['start'], form.cleaned_data['mutated_allele'], form.cleaned_data['liftover'])
            else:
                get_string='?reference={}&chromosome={}&start={}&mutated_allele={}&liftover={}'.format(form.cleaned_data['reference'], form.cleaned_data['chromosome'], form.cleaned_data['start'], form.cleaned_data['mutated_allele'], form.cleaned_data['liftover'])


            return HttpResponseRedirect('/' + get_string)
        else:
           raise TypeError("can't fill mutated allele if region is specified")
        
    if request.method == 'GET':
        print('getting')
        LOG.debug('getting')
        check = 0
        params = dict(request.GET)
        print(params)
        LOG.debug(params)
        for k,v in params.items():
            if k == 'reference':
                check += 1
            if k == 'chromosome':
                check += 1
            if k == 'start':
                check += 1
        if check > 2:
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

            listin = return_list(params['reference'], params['chromosome'], params['start'], params['region'], params['mutated_allele'], params['liftover'])
            print(listin)
            LOG.debug(listin)
            references=['37','38']
            chromosomess=[str(x) for x in range(1, 23)] + ["X", "Y", "MT"]
            liftovers=["'LIFTOVER'", "''"]
            


            if listin[0] not in references:
                return HttpResponseBadRequest('Bad Request')
            if listin[1] not in chromosomess:
                return HttpResponseBadRequest('Bad Request')
            
            if listin[2] == '':
                pass
            else:
                try:
                    if int(listin[2]) <= 99999999999:
                        pass
                    else:
                        return HttpResponseBadRequest('Bad Request')
                except Exception:
                        return HttpResponseBadRequest('Bad Request')
            
            if listin[3] == '':
                pass
            else:
                try:
                    if int(listin[3]) <= 10000:
                        pass
                    else:
                        return HttpResponseBadRequest('Bad Request')
                except Exception:
                    return HttpResponseBadRequest('Bad Request')
            
            


            if listin[5] not in liftovers:

                return HttpResponseBadRequest('Bad Request')
            
            print(current_email)
                

            dict_complete = return_datasets(params['reference'], params['chromosome'], params['start'], params['region'], params['mutated_allele'], params['liftover'], current_email)
            boolean = dict_complete["boolean"]
            del dict_complete["boolean"]
            num_results = dict_complete["num_results"]
            del dict_complete["num_results"]
            num_datasets = dict_complete["num_datasets"]
            del dict_complete["num_datasets"]


            context = {
                    'string': return_string(params['reference'], params['chromosome'], params['start'], params['region'], params['mutated_allele'], params['liftover'], current_email),
                    'boolean': boolean,
                    'num_results': num_results,
                    'datasets': dict_complete,
                    'num_datasets': num_datasets,
                    'form': form


                }
            
            timestr = time.strftime("%Y%m%d")
            file_name = timestr
            path = '/logs/' + file_name + '.txt'
            file = open(path, 'a+')  # 'a+' mode instead of 'w' mode
            file.write(return_string(params['reference'], params['chromosome'], params['start'], params['region'], params['mutated_allele'], params['liftover'], current_email) + ' GET' + '\n')
            file.close()

            return render(request, 'base.html', context)
            
    
    return render(request, template, context)

def bash_true_view(request):
    template = "home.html"
    form =BamFormTrue()
    context = {'form': form}
    if request.user.is_authenticated:
        current_email=request.user.email
        print(current_email)
        LOG.debug(current_email)
    else:
        current_email = ''
    if request.method == 'POST':
        form = BamFormTrue(request.POST)
        if form.is_valid():
            if form.cleaned_data['region'] != None and form.cleaned_data['mutated_allele'] != '':
                get_string='?reference={}&chromosome={}&start={}&region={}&mutated_allele={}&liftover={}'.format(form.cleaned_data['reference'], form.cleaned_data['chromosome'], form.cleaned_data['start'], form.cleaned_data['region'], form.cleaned_data['mutated_allele'], form.cleaned_data['liftover'])
            elif form.cleaned_data['region'] != None:
                get_string='?reference={}&chromosome={}&start={}&region={}&liftover={}'.format(form.cleaned_data['reference'], form.cleaned_data['chromosome'], form.cleaned_data['start'], form.cleaned_data['region'], form.cleaned_data['liftover'])
            elif form.cleaned_data['mutated_allele'] != '':
                get_string='?reference={}&chromosome={}&start={}&mutated_allele={}&liftover={}'.format(form.cleaned_data['reference'], form.cleaned_data['chromosome'], form.cleaned_data['start'], form.cleaned_data['mutated_allele'], form.cleaned_data['liftover'])
            else:
                get_string='?reference={}&chromosome={}&start={}&mutated_allele={}&liftover={}'.format(form.cleaned_data['reference'], form.cleaned_data['chromosome'], form.cleaned_data['start'], form.cleaned_data['mutated_allele'], form.cleaned_data['liftover'])


            return HttpResponseRedirect('/' + get_string)
        
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
        if check > 2:
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

            listin = return_list(params['reference'], params['chromosome'], params['start'], params['region'], params['mutated_allele'], params['liftover'])
            references=['37','38']
            chromosomess=[str(x) for x in range(1, 23)] + ["X", "Y", "MT"]
            liftovers=["'LIFTOVER'", "''"]
            


            if listin[0] not in references:
                return HttpResponseBadRequest('Bad Request')
            if listin[1] not in chromosomess:
                return HttpResponseBadRequest('Bad Request')
            
            if listin[2] == '':
                pass
            else:
                try:
                    if int(listin[2]) <= 99999999999:
                        pass
                    else:
                        return HttpResponseBadRequest('Bad Request')
                except Exception:
                        return HttpResponseBadRequest('Bad Request')
            
            if listin[3] == '':
                pass
            else:
                try:
                    if int(listin[3]) <= 10000:
                        pass
                    else:
                        return HttpResponseBadRequest('Bad Request')
                except Exception:
                    return HttpResponseBadRequest('Bad Request')
            

            


            if listin[5] not in liftovers:

                return HttpResponseBadRequest('Bad Request')
                
            dict_complete = return_datasets(params['reference'], params['chromosome'], params['start'], params['region'], params['mutated_allele'], params['liftover'], current_email)
            boolean = dict_complete["boolean"]
            del dict_complete["boolean"]
            num_results = dict_complete["num_results"]
            del dict_complete["num_results"]
            num_datasets = dict_complete["num_datasets"]
            del dict_complete["num_datasets"]


            context = {
                    'string': return_string(params['reference'], params['chromosome'], params['start'], params['region'], params['mutated_allele'], params['liftover'], current_email),
                    'boolean': boolean,
                    'num_results': num_results,
                    'datasets': dict_complete,
                    'num_datasets': num_datasets,
                    'form': form


                }
            
            timestr = time.strftime("%Y%m%d")
            file_name = timestr
            path = '/logs/' + file_name + '.txt'
            file = open(path, 'a+')  # 'a+' mode instead of 'w' mode
            file.write(return_string(params['reference'], params['chromosome'], params['start'], params['region'], params['mutated_allele'], params['liftover'], current_email) + ' GET' + '\n')
            file.close()

            return render(request, 'base.html', context)
            
    
    return render(request, template, context)

def bash_false_view(request):
    template = "home.html"
    form =BamFormFalse()
    context = {'form': form}
    if request.user.is_authenticated:
        current_email=request.user.email
        print(current_email)
        LOG.debug(current_email)
    else:
        current_email = ''
    if request.method == 'POST':
        form = BamFormFalse(request.POST)
        if form.is_valid():
            if form.cleaned_data['region'] != None and form.cleaned_data['mutated_allele'] != '':
                get_string='?reference={}&chromosome={}&start={}&region={}&mutated_allele={}&liftover={}'.format(form.cleaned_data['reference'], form.cleaned_data['chromosome'], form.cleaned_data['start'], form.cleaned_data['region'], form.cleaned_data['mutated_allele'], form.cleaned_data['liftover'])
            elif form.cleaned_data['region'] != None:
                get_string='?reference={}&chromosome={}&start={}&region={}&liftover={}'.format(form.cleaned_data['reference'], form.cleaned_data['chromosome'], form.cleaned_data['start'], form.cleaned_data['region'], form.cleaned_data['liftover'])
            elif form.cleaned_data['mutated_allele'] != '':
                get_string='?reference={}&chromosome={}&start={}&mutated_allele={}&liftover={}'.format(form.cleaned_data['reference'], form.cleaned_data['chromosome'], form.cleaned_data['start'], form.cleaned_data['mutated_allele'], form.cleaned_data['liftover'])
            else:
                get_string='?reference={}&chromosome={}&start={}&mutated_allele={}&liftover={}'.format(form.cleaned_data['reference'], form.cleaned_data['chromosome'], form.cleaned_data['start'], form.cleaned_data['mutated_allele'], form.cleaned_data['liftover'])


            return HttpResponseRedirect('/' + get_string)
        
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
        if check > 2:
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

            listin = return_list(params['reference'], params['chromosome'], params['start'], params['region'], params['mutated_allele'], params['liftover'])
            references=['37','38']
            chromosomess=[str(x) for x in range(1, 23)] + ["X", "Y", "MT"]
            liftovers=["'LIFTOVER'", "''"]
            


            if listin[0] not in references:
                return HttpResponseBadRequest('Bad Request')
            if listin[1] not in chromosomess:
                return HttpResponseBadRequest('Bad Request')
            
            if listin[2] == '':
                pass
            else:
                try:
                    if int(listin[2]) <= 99999999999:
                        pass
                    else:
                        return HttpResponseBadRequest('Bad Request')
                except Exception:
                        return HttpResponseBadRequest('Bad Request')
            
            if listin[3] == '':
                pass
            else:
                try:
                    if int(listin[3]) <= 10000:
                        pass
                    else:
                        return HttpResponseBadRequest('Bad Request')
                except Exception:
                    return HttpResponseBadRequest('Bad Request')
            

            


            if listin[5] not in liftovers:

                return HttpResponseBadRequest('Bad Request')
                

            dict_complete = return_datasets(params['reference'], params['chromosome'], params['start'], params['region'], params['mutated_allele'], params['liftover'], current_email)
            boolean = dict_complete["boolean"]
            del dict_complete["boolean"]
            num_results = dict_complete["num_results"]
            del dict_complete["num_results"]
            num_datasets = dict_complete["num_datasets"]
            del dict_complete["num_datasets"]


            context = {
                    'string': return_string(params['reference'], params['chromosome'], params['start'], params['region'], params['mutated_allele'], params['liftover'], current_email),
                    'boolean': boolean,
                    'num_results': num_results,
                    'datasets': dict_complete,
                    'num_datasets': num_datasets,
                    'form': form


                }
            
            timestr = time.strftime("%Y%m%d")
            file_name = timestr
            path = '/logs/' + file_name + '.txt'
            file = open(path, 'a+')  # 'a+' mode instead of 'w' mode
            file.write(return_string(params['reference'], params['chromosome'], params['start'], params['region'], params['mutated_allele'], params['liftover'], current_email) + ' GET' + '\n')
            file.close()

            return render(request, 'base.html', context)
            
    
    return render(request, template, context)
# Create your views here.
