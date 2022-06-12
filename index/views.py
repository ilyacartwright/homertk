from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import Http404
from django.shortcuts import render
from .models import CompanyGoal

def render_index_page(request):

    goal = CompanyGoal.objects.all()
    # department = Department.objects.all()
    return render(request, 'page/home.html', {
        'goal': goal,
        }
    )

# class HomePage(TemplateView):
#     template_name = "page/home.html"

