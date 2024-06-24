from django.contrib import admin

# Register your models here.
from . import models
# Register your models here.

@admin.register(models.Template)
class TemplateAdmin(admin.ModelAdmin):
    list_display=('id','name','content','date')


@admin.register(models.Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display=('id','company', 'template', 'budget', 'status','date')


@admin.register(models.Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display=('id','company_name','industry')


@admin.register(models.CampaignCustomers)
class CampaignCustomersAdmin(admin.ModelAdmin):
    list_display=('id',)

