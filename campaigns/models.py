from django.db import models
from django.db.models import CASCADE
from datetime import datetime


# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=50, null=True, blank=True, default='')
    last_name = models.CharField(max_length=50, null=True, blank=True, default='')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    # 1-1 relationship between customer and company, using Charfield for testing
    company = models.CharField(max_length=100, default='', null=True, blank=True)

    class Meta:
        db_table = "customer"


class Company(models.Model):
    company_name = models.CharField(max_length=100, null=True, blank=True, default='')
    industry = models.CharField(max_length=100, null=True, blank=True, default='')

    class Meta:
        db_table = "company"


class Template(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    content = models.TextField(null=False, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "template"


class Campaign(models.Model):
    # 1-1 relationship between campaign and company, using Charfield for testing
    company = models.CharField(max_length=100, default='', null=True, blank=True)
    template = models.OneToOneField(Template, db_column='template_id', null=True, on_delete=CASCADE,
                                    related_name='campaign_template')
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "campaign"


class CampaignCustomers(models.Model):
    campaign = models.ForeignKey(Campaign, db_column='campaign_id', null=False, on_delete=CASCADE,
                                 related_name='campaign_related')
    customer = models.ForeignKey(Customer, db_column='customer_id', null=False, on_delete=CASCADE,
                                 related_name='campaign_customer')

    class Meta:
        db_table = "campaign_customers"
