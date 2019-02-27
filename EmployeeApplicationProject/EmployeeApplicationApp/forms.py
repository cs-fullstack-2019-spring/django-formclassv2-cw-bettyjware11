from django import forms

# Create your forms here.
class EmployeeApplicationForm(forms.Form):
    name = forms.CharField()
    dateOfBirth = forms.IntegerField()
    positionApplyingTo = forms.CharField()
    salary = forms.IntegerField()

