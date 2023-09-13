from typing import Any
from wsgiref.validate import validator
from django import forms 
from django.core import validators

def check_for_name(value):
    if value[0]=='S':
        raise forms.ValidationError('Name start with S')
    
def check_for_len(value):
    if len(value)<5:
        raise forms.ValidationError('Length < 5')

def check_for_age(value):
    if value<18:
        raise forms.ValidationError('Age is <18')
    


class StudentForm(forms.Form):
    Sname=forms.CharField(max_length=10,validators=[check_for_name,check_for_len])
    Sage=forms.IntegerField(validators=[check_for_age])
    Semail=forms.EmailField()
    Re_enter_email=forms.EmailField()
    Mobile=forms.CharField(max_length=10,min_length=10,validators=[validators.RegexValidator('[6-9]\d{9}')])
    Bot_catcher=forms.CharField(max_length=100,widget=forms.HiddenInput,required=False)

    def clean(self):
        e=self.cleaned_data['Semail']
        re=self.cleaned_data['Re_enter_email']
        if (e!=re):
            raise forms.ValidationError('Emails not matched')

    def clean_Bot_catcher(self):
        bot=self.cleaned_data['Bot_catcher']
        if len(bot)>0:
            raise forms.ValidationError('bot>0')
        