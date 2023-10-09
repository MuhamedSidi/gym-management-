from datetime import datetime
from dateutil.relativedelta import relativedelta
from django.db import models,transaction
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils.translation import gettext_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput,TextInput
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from django.contrib.auth .forms import UserChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from datetime import date






class Gender(models.TextChoices):
    MALE = 'male', 'Male'
    FEMALE = 'female', 'Female'
# class LoginForm(AuthenticationForm):
#     username = forms.CharField(widget=TextInput)
#     password = forms.CharField(widget=PasswordInput())


# class User():
#     username = models.CharField(max_length=100)
#     password = models.CharField(max_length=50)

class UserProfile(models.Model):
    username = models.CharField(max_length=100)
    phone_number =  models.CharField(max_length=100)
    password = models.CharField(max_length=100)
     # Define unique related_name attributes
    # groups = models.ManyToManyField(
    #     'auth.Group',
    #     related_name='custom_user_set',
    #     blank=True,
    #     verbose_name='groups',
    #     help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    # )

    # user_permissions = models.ManyToManyField(
    #     'auth.Permission',
    #     related_name='custom_user_set',
    #     blank=True,
    #     verbose_name='user permissions',
    #     help_text='Specific permissions for this user.',
    # )



    

    # groups = models.ManyToManyField(
    #     Group,
    #     verbose_name=gettext_lazy('groups'),
    #     blank=True,
    #     related_name='custom_admins_groups'  # Use a unique related_name
    # )
    # user_permissions = models.ManyToManyField(
    #     Permission,
    #     verbose_name=gettext_lazy('user permissions'),
    #     blank=True,
    #     related_name='custom_admins_permissions'  # Use a unique related_name
    # )

    # def __str__(self):
    #     return self.name

    # # Define a related_name for groups and user_permissions
    # groups = models.ManyToManyField(
    #     Group,
    #     verbose_name=gettext_lazy('groups'),
    #     blank=True,
    #     related_name='custom_admins'  # Use a unique related_name
    # )
    # user_permissions = models.ManyToManyField(
    #     Permission,
    #     verbose_name=gettext_lazy('user permissions'),
    #     blank=True,
    #     related_name='custom_admins'  # Use a unique related_name
    # )

   
class Subscriber(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=11)
    image = models.ImageField(upload_to='subscriber_images')
    gender = models.CharField(max_length=10, choices=Gender.choices)
    salary = models.FloatField()
    subscription_date = models.DateField()
    how_many_month = models.IntegerField()
    expired_date = models.DateField(null=True, blank=True)  # Add this field

    def __str__(self):
        return f"{self.name} - {self.gender} - {self.subscription_date}"
    

    @property
    def is_subscription_expired(self):
        return self.expired_date < date.today()
    

    @classmethod
    def get_total_subscribers(cls):
        try:
            total_subscribers = cls.objects.count()
            return total_subscribers
        except cls.DoesNotExist:
            return 0

    def calculate_expired_date(self):
        self.expired_date = self.subscription_date + relativedelta(months=self.how_many_month)
    @classmethod
    def get_total_salary(cls):
        try:
            total_salary = cls.objects.aggregate(models.Sum('salary'))['salary__sum']
            return total_salary if total_salary else 0
        except cls.DoesNotExist:
            return 0
    
    @classmethod
    def get_expired_subscribers_count(cls):
        try:
            expired_subscribers_count = cls.objects.filter(expired_date__lt=date.today()).count()
            return expired_subscribers_count
        except cls.DoesNotExist:
            return 0
        

        
    def save(self, *args, **kwargs):
        self.calculate_expired_date()
        super().save(*args, **kwargs)



