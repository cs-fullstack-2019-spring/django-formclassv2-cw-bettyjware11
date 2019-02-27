from django.shortcuts import render
from django.shortcuts import HttpResponse
from .forms import EmployeeApplicationForm


# this function is used to test whether the server is working
def index(request):
    return HttpResponse("EmployeeApplicationApp")

# function puts info into new form
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

# this function extracts information, saves and  puts it in a new form
def application(request):

    if(request.method == 'POST'):
        print(request.POST)
        newForm = EmployeeApplicationForm(request.POST)
        if newForm.is_valid():
            newForm.save(commit=True)
        context = {"name": request.POST["name"]}
        return render(request, "EmployeeApplicationApp/listEmployeeInfo.html", context)
    else:
        newForm = EmployeeApplicationForm()
        context = {
            "newForm": newForm,
        }
        return render(request, "EmployeeApplicationApp/Index.html", context)
