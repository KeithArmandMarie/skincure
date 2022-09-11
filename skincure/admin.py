from django.contrib import admin
from skincure.models import SkinDisease, Treatment
# Register your models here.
@admin.register(SkinDisease)
class skinDiseaseAdmin(admin.ModelAdmin):
    list_display = ['name']
@admin.register(Treatment)
class TreatmentAdmin(admin.ModelAdmin):
    list_display = ['id','description']