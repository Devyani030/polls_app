from django import forms


class NameForm(forms.Form):
    Your_Question = forms.CharField(max_length=500)
    Choice_1 = forms.CharField(max_length=100)
    Choice_2 = forms.CharField(max_length=100)
    Choice_3= forms.CharField(max_length=100)
    Choice_4= forms.CharField(max_length=100)