from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
# from .forms import CustomAdminCreationForm 
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
# from .forms import userAdmin
from django.contrib.auth import authenticate, login

from django.shortcuts import render, redirect

# appname/views.py
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.forms import inlineformset_factory

# appname/views.py
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth.models import User
from django.contrib import messages  
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,logout,authenticate

from .models import Subscriber
from django.contrib.auth import login, authenticate
from django.contrib.auth import login, authenticate
from django.shortcuts import render  # Import render function



# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Subscriber
from .forms import SubscriberForm
# from .forms import SubscriberUpdateForm

# Add this view to update a user
from .forms import SubscriberUpdateForm
from .models import Subscriber


# Add this view to delete a user
# views.py

# ...

from django.shortcuts import get_object_or_404, redirect
from .models import Subscriber

# Add this view to delete a subscriber







from .models import User  # Import your User model

from django.shortcuts import render
from django.views.generic import ListView 
from .models import Subscriber
import json


   

from django.shortcuts import render
from django.db.models import Q
from .models import Subscriber
from django.shortcuts import render
from django.db.models import Q
from .models import Subscriber
from django.views.generic import ListView
from .forms import SubscriberSearchForm



### delete users admin

def delete_user(request,pk):
     user = User.objects.filter(id=pk)
     user.delete()
     return redirect('user_list')



































from django.shortcuts import render
from .models import Subscriber

# def your_view(request):
   
from reportlab.lib.styles import getSampleStyleSheet

styles = getSampleStyleSheet()
from io import BytesIO
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from .models import Subscriber  # Import your Subscriber model here

def generate_pdf(request):
    # Create a file-like buffer to receive PDF data.
    buffer = BytesIO()

    # Create the PDF object, using the BytesIO buffer as its "file."
    doc = SimpleDocTemplate(buffer)

    # Create a list to hold the elements of the PDF (e.g., tables, paragraphs)
    elements = []

    # Collect data (e.g., total money, number of users, expired subscribers)
    total_salary = Subscriber.get_total_salary()  # Get the total money from subscribers
    total_subscribers = Subscriber.get_total_subscribers()  # Get the total number of users
    expired_subscribers_count = Subscriber.get_expired_subscribers_count()  # Get the count of expired subscribers

    # Define styles for the title and body text
    styles = getSampleStyleSheet()
    title_style = styles['Title']

    # Add a title to the PDF
    title = Paragraph("Subscriber Information Report", style=title_style)
    elements.append(title)

    # Create a table to display the data
    data = [
        ["Total Money", f"${total_salary}"],
        ["Number of Users", total_subscribers],
        ["Expired Subscribers", expired_subscribers_count],
    ]

    # Create the table and set its style
    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))

    # Add the table to the PDF elements
    elements.append(table)

    # Build the PDF document
    doc.build(elements)

    # FileResponse sets the Content-Disposition header for download
    buffer.seek(0)
    response = FileResponse(buffer, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="subscriber_report.pdf"'

    return response


















#search in subscribers

def search_subscribers(request):
    form = SubscriberSearchForm(request.GET)
    subscribers = Subscriber.objects.all()

    if form.is_valid():
        name = form.cleaned_data.get('name')
        if name:
            subscribers = subscribers.filter(name__icontains=name)
            # Add more filtering logic for other fields

    return render(request, 'html/search_list.html', {'subscribers': subscribers})
    




































# Show subscriber functions 
from django.contrib.auth import login as auth_login
# def log_out(request):
from .models import Subscriber  # Import the Subscriber model from your app

def list_Man(request):
    # Filter the subscribers to only include males
    male_subscribers = Subscriber.objects.filter(gender='male')
    context = {'posts': male_subscribers}
    return render(request, 'html/list_Male.html', context)
def list_Female(request):
    # Filter the subscribers to only include males
    male_subscribers = Subscriber.objects.filter(gender='female')
    context = {'posts': male_subscribers}
    return render(request, 'html/list_fm.html', context)



#

def user_list(request):
    users = User.objects.all()
    return render(request, 'html/List_admin.html', {'users': users})















#log in fucntions 



def log_in(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
      # Call the Django built-in login() function
      auth_login(request, user)
      return redirect('home')

  context = {}
  return render(request, 'html/login.html', context)

# views.py
from django.shortcuts import render, redirect
from .forms import SubscriberForm



from .models import Subscriber

# update subcriber 

from django.shortcuts import render, redirect, get_object_or_404
from .models import Subscriber
from .forms import SubscriberForm
import os 
from .models import Subscriber  # You should import your Subscriber model here
from django.urls import reverse_lazy 

def update_subscriber(request,pk):
    subscriber = Subscriber.objects.get(id=pk)
    form = SubscriberForm(instance=subscriber)
    if request.method == 'POST':
        form = SubscriberForm(request.POST, request.FILES,instance=subscriber)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form':form}
    
    return render(request, 'html/update-user.html')





















from django.shortcuts import render
from .models import Subscriber

from django.shortcuts import render
from .models import User  # Replace 'User' with your actual model name

# def search_list(request):
#     subscriber_query = request.GET.get('subscriber', '')
#     # Perform a query to retrieve the desired users based on the 'subscriber' parameter
#     search_results = Subscriber.objects.filter(name__icontains=subscriber_query)
    
#     context = {
#         'search_results': search_results,
#     }
    
#     return render(request, 'html/search_list.html', context)
















#delete subscriber 

def delete_subscriber(request,pk):
     subscriber = Subscriber.objects.filter(id=pk)
     subscriber.delete()
     return redirect('home')







# add subscriber 


def add_subscriber(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
       
    else:
        form = SubscriberForm()
    
    return render(request, 'html/add-user.html', {'form': form})





#save admin


def register_admin(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
                form.save()
                return render(request,'html/login.html')
            
            # Redirect to a success page or home page
    else:
        form = UserRegistrationForm()
    return render(request, 'html/add-admin.html', {'form': form})

#home page 
def home(request):
    total_subscribers = Subscriber.get_total_subscribers()
    total_salary = Subscriber.get_total_salary()
    expired_subscribers_count = Subscriber.get_expired_subscribers_count()
    context = {
    'total_subscribers': total_subscribers,
    'total_salary': total_salary,
    'expired_subscribers_count': expired_subscribers_count,
}
   
    return render(request, 'html/dashboard.html',context)   
def login(request):
    return render(request,'html/login.html')
def addu(request):
    return render(request,"html/add-user.html")
def adda(request):
    return render (request,"html/add-admin.html")






