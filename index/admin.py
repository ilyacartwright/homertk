from django.contrib import admin
from .models import CompanyGoal, Department, DeparmentList

@admin.register(CompanyGoal)
class CompanyGoalAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'active')

class DeparmentListInline(admin.TabularInline):

    model = DeparmentList
    extra = 0

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'active')
    inlines = [DeparmentListInline]

