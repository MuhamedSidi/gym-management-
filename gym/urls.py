from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views 
urlpatterns = [
    path('',views.login),
    path('home/',views.home,name='home'),
    # path('addu/',views.addu),
    path('addu', views.addu, name='addu'),
    path('adda', views.adda, name='adda'),  
    path('list_Female/', views.list_Female, name='list_Female'),
    path('register_admin/', views.register_admin, name='register_admin'),
    path('log_in/', views.log_in, name='log_in'),
    path('add_subscriber/', views.add_subscriber, name='add_subscriber'),
    path('list_Man/', views.list_Man, name='list_Man'),
    path('user_list/', views.user_list, name='user_list'),
    path('update_subscriber/<str:pk>/', views.update_subscriber, name='update_subscriber'),
    path('delete_subscriber/<str:pk>/', views.delete_subscriber, name='delete_subscriber'),
    path('search_subscribers/', views.search_subscribers,name='search_subscribers'),
    path('generate_pdf/', views.generate_pdf, name='generate_pdf'),
    path('delete_user/<str:pk>/', views.delete_user, name='delete_user'),




]
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)