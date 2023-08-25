from django.contrib import admin
from .models import EvaluateForm

class EvaluateFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'last_name', 'email','date_of_birth')

admin.site.register(EvaluateForm, EvaluateFormAdmin)
