from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', include('gym.urls')),
    # path('addadmin/',include('authentification.urls')),
    path('admin/',admin.site.urls),
    # path('register_admin/', include('gym.urls')),
    # path('addu/',include('gym.urls')),
    ]


