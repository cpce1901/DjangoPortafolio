from django.urls import path
from .views import Home

app_name = 'app_core'

#URLs app CORE
urlpatterns = [
    path('', Home.as_view(), name='home'),
]