from datetime import datetime

from django.urls import path
from .views import render_index_page

app_name = 'index'


urlpatterns = [
    path('', render_index_page, name="home"),

]
