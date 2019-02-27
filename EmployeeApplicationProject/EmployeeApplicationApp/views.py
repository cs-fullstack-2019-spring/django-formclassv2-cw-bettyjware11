from django.shortcuts import render
from django.shortcuts import HttpResponse
from .forms import EmployeeApplicationForm

# Create your views here.

# this function is used to test whether the server is working
def index(request):
    return HttpResponse("EmployeeApplicationApp")

def applicationForm(request):
    newForm = EmployeeApplicationForm()

    context = {
        "newForm": newForm
    }

    return render(request, "EmployeeApplicationApp/index.html", context)

# this function prints the employee info
def listEmployeeInfo(request):
    print(request.POST)
    print(request.POST["name"])
    return HttpResponse("Listed Employee Info")

def application(request):

    if(request.method == 'POST'):
        print(request.POST)
        context = {"name": request.POST["name"]}
        return render(request, "EmployeeApplicationApp/listEmployeeInfo.html", context)
    else:
        newForm = EmployeeApplicationForm()
        context = {
            "newForm": newForm,
        }
        return render(request, "EmployeeApplicationApp/Index.html", context)
