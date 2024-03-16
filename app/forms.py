from django.forms import ModelForm
from .models import CustomUser



class WorkerEditForm(ModelForm):
    class meta:
        model = CustomUser
        fields = ['first_name','last_name','email','phone_number','address','description','username']

class EmployerEditForm(ModelForm):
    class meta:
        model = CustomUser
        fields = ['first_name','last_name','email','phone_number','address','description','username']