from datetime import datetime

from django.urls import path
from .views import HomePage

app_name = 'index'


urlpatterns = [
    path('', HomePage.as_view(), name="home"),

]
