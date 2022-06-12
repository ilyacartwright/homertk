from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import Http404
from django.shortcuts import render
from .models import CompanyGoal, Deparment, Footer

def render_index_page(request):

    goal = CompanyGoal.objects.all()
    deparment = Deparment.objects.all()
    footer = Footer.objects.all()
    return render(request, 'page/home.html', {
        'goal': goal,
        'deparment': deparment,
        'footer': footer,
        }
    )

# class HomePage(TemplateView):
#     template_name = "page/home.html"

