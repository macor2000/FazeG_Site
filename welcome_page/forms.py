from django import forms
#Defining a form class with three fields.
class ApplicationForm(forms.Form):
    your_name = forms.CharField(label = "Your name", max_length=100)
    your_dob = forms.DateField(label = "Your date of birth")
    your_email = forms.EmailField(label = "Your email address", max_length=100)
