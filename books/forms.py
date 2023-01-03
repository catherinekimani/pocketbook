from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# forms
class NewUserForm(UserCreationForm):
    email=forms.EmailField(required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
        
    def __init__(self,*args, **kwargs):
        super(NewUserForm, self).__init__(*args,**kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control' 
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
