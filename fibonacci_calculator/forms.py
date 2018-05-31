from django import forms


class InputForm(forms.Form):
    number_input = forms.IntegerField()