from django import forms
from .models import Account

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'رمز را وارد کنید'
    }))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'تکرار رمز ورود'
    }))

    class Meta:
        model=Account
        fields=['first_name','last_name','phone_number','email','password']
    def __init__(self,*args,**kwargs):
        super(RegistrationForm,self).__init__(*args,**kwargs)
        self.fields['first_name'].widget.attrs['placeholder'] = 'نام شما'
        self.fields['email'].widget.attrs['placeholder'] = 'ایمیل شما'
        self.fields['last_name'].widget.attrs['placeholder'] = 'نام خانوادگی شما'
        self.fields['phone_number'].widget.attrs['placeholder'] ='تلفن تماس'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'