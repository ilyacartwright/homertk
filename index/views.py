from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import Http404
from django.shortcuts import render
from .models import CompanyGoal, Department

class Testik(TemplateView):
    template_name = 'page/home.html'

def render_index_page(request):

    goal = CompanyGoal.objects.all()
    department = Department.objects.all()

    return render(request, 'page/home.html', {
        'goal': goal,
        'department': department,
        }
    )
