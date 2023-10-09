from django.contrib import admin
from .models import Subscriber
# from .forms import userAdmin

# class myAdmin(admin.ModelAdmin):
#     readonly_fields=('id',)
# admin.site.register(Admin,myAdmin)

admin.site.register(Subscriber)
# admin.site.register(Expired)