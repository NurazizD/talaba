from django.contrib import admin
from .models import Pupil
# Register your models here.
class Pupil_admin(admin.ModelAdmin):
    list_display = ['ism','yosh','tugulgan_kun','guruh','tel_raqam']
admin.site.register(Pupil,Pupil_admin)