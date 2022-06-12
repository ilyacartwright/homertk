from datetime import datetime

from django.urls import path
from .views import render_index_page, Testik

app_name = 'index'


urlpatterns = [
    path('', Testik.as_view(), name="home"),

]
