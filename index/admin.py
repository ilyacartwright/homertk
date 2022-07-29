from django.contrib import admin
from .models import CompanyGoal, Deparment, DeparmentList, Footer, FooterList, Vakance, VakanceCriteria

@admin.register(CompanyGoal)
class CompanyGoalAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'active')

class DeparmentListInline(admin.TabularInline):

    model = DeparmentList
    extra = 0

@admin.register(Deparment)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'active')
    inlines = [DeparmentListInline]

class FooterListInline(admin.TabularInline):

    model = FooterList
    extra = 1

@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    list_display = ('title', 'active')
    inlines = [FooterListInline]

class VakanceCriteriaInline(admin.TabularInline):

    model = VakanceCriteria
    extra = 1

@admin.register(Vakance)
class VakanceAdmin(admin.ModelAdmin):
    list_display = ('title', 'active')
    inlines = [VakanceCriteriaInline]