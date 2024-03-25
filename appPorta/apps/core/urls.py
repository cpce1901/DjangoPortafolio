from django.urls import path
from .views import Home

app_name = 'core_app'

#URLs app CORE
urlpatterns = [
    path('', Home.as_view(), name='home'),
]