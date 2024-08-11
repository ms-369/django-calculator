from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

from django import forms



def calculation(request):
    num1=""
    num2=""
    result=""
    op=""
    try:
        if request.method == 'POST':
            num1 = int(request.POST.get("input1"))
            num2 = int(request.POST.get("input2"))
            op = request.POST.get("operation")
            if op == "add":
                result=num1+num2
            elif op == "sub":
                result=num1-num2
            elif op == "mul":
                result=num1*num2
            elif op == "div":
                if num2 != 0:
                    result=num1/num2
                else:
                    result="error"
    except:
        print("ERRROOORRR")

    print(result)
    return render(request,"pages/home.html",{"num1":num1,"num2":num2,"result":result,"op":op})