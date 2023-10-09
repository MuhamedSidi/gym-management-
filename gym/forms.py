from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models


from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms
from django.contrib.auth.forms import UserCreationForm
 # Import your custom Admin model
from django import forms
from .models import UserProfile

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Subscriber

# forms.py
from django import forms
from .models import Subscriber



# forms.py

from django import forms
from .models import Subscriber

class SubscriberUpdateForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['name', 'phone_number', 'image', 'gender', 'salary', 'subscription_date', 'how_many_month']

class SubscriberSearchForm(forms.Form):
    name = forms.CharField(max_length=200, required=False)
































class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = '__all__'

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.calculate_expired_date()
        if commit:
            instance.save()
        return instance



class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')




