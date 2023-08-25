from django.urls import path
from .views import submit_data

urlpatterns = [
    path('submit_data/', submit_data, name='submit_data'),
]
