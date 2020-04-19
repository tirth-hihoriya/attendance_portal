from django.shortcuts import render, redirect, get_object_or_404
import csv, io
from django.contrib import messages
import decimal
from .models import *



def csv_upload(request):
    template= 'portal/csv_upload.html'

    prompt = {
        'csv': 'it should be csv'

    }

    if request.method == "GET":
        return render(request, template, prompt)

    csv_file = request.FILES['file']

    if not csv_file.name.endswith('.csv'):
        messages.error(request,'This is not a csv file...!!')

    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)

    for row in csv.reader(io_string,delimiter=',',quotechar='|'):
        total_days = len(row)-1
        rollno1 = row[0]
        present = row.count('p')
        percent = present/total_days*100
        print(rollno1 + "    " + str(total_days) + "      " + str(present) + "      " + str(percent) + "%")
        
        lt65 = False
        lt85 = False
        if percent<65:
            lt65 = True
        elif percent<85:
            lt85 = True
        else:
            lt65 = False
            lt85 = False

        _, created = Result.objects.update_or_create(
            rollno = rollno1,
            working_days = total_days,
            present_days = present ,
            percentage  = decimal.Decimal(percent) ,
            lessthan_85 = lt85,
            lessthan_65 = lt65,

        )

    context = {}

    return render(request, template, context)



def home(request):
    template= 'portal/home.html'
    rows = Result.objects.all()
    context = {
        'rows': rows,
       
    }
    return render(request, template, context)
