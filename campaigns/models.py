from django.db import models
from django.db.models import CASCADE
from datetime import datetime


# Create your models here.


class Company(models.Model):
    company_name = models.CharField(max_length=100, null=True, blank=True, default='')
    industry = models.CharField(max_length=100, null=True, blank=True, default='')

    class Meta:
        db_table = "company"


class Customer(models.Model):
    first_name = models.CharField(max_length=50, null=True, blank=True, default='')
    last_name = models.CharField(max_length=50, null=True, blank=True, default='')
    created_on = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=50, default='new', choices=[('new', 'New'), ('regular', 'Regular'), ('vip', 'VIP')],  null=False, blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    company = models.ForeignKey(Company, db_column='company_id', null=True, on_delete=CASCADE,
                                    related_name='customer_company')

    class Meta:
        db_table = "customer"

class Template(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "template"


class Campaign(models.Model):
    # 1-1 relationship between campaign and company, using Charfield for testing
    name = models.CharField(max_length=100, default='', null=False, blank=True)
    budget = models.IntegerField(default=0, null=True, blank=True)
    status = models.CharField(max_length=50, default='draft', choices=[('draft', 'Draft'), ('prepared', 'Prepared'), ('active', 'Active'), ('completed', 'Completed')],  null=False, blank=True)
    company = models.ForeignKey(Company, db_column='company_id', null=True, on_delete=CASCADE,
                                    related_name='campaign_company')
    template = models.OneToOneField(Template, db_column='template_id', null=True, on_delete=CASCADE,
                                    related_name='campaign_template')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "campaign"


class CampaignCustomers(models.Model):
    campaign = models.ForeignKey(Campaign, db_column='campaign_id', null=False, on_delete=CASCADE,
                                 related_name='campaign_related')
    customer = models.ForeignKey(Customer, db_column='customer_id', null=False, on_delete=CASCADE,
                                 related_name='campaign_customer')

    class Meta:
        db_table = "campaign_customers"
