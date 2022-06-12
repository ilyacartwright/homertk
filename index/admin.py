from django.contrib import admin
from .models import CompanyGoal

@admin.register(CompanyGoal)
class CompanyGoalAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'active')
