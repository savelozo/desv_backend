from django.urls import path
from .views import submit_data_view

urlpatterns = [
    path('submit_data/', submit_data_view, name='submit_data'),
]
