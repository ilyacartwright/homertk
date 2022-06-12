from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import Http404
from django.shortcuts import render
from .models import CompanyGoal, Deparment, Footer, Vakance
from newsapp.models import New


def render_index_page(request):

    goal = CompanyGoal.objects.all()
    deparment = Deparment.objects.all()
    footer = Footer.objects.all()
    vakance = Vakance.objects.all()
    news = New.objects.all()[:3]
    return render(request, 'page/home.html', {
        'goal': goal,
        'deparment': deparment,
        'footer': footer,
        'vakance': vakance,
        'news': news,
        }
    )

# class HomePage(TemplateView):
#     template_name = "page/home.html"

