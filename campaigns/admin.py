from django.contrib import admin

# Register your models here.
from . import models
# Register your models here.

@admin.register(models.Template)
class TemplateAdmin(admin.ModelAdmin):
    list_display=('id','name','content','created_on')


@admin.register(models.Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display=('id','created_on')


@admin.register(models.Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display=('id','company_name','industry')


@admin.register(models.CampaignCustomers)
class CampaignCustomersAdmin(admin.ModelAdmin):
    list_display=('id',)

