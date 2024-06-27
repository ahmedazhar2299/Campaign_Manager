from django.urls import path

from .Views.CampaignView import *
from .Views.TemplateView import *
from .Views.CompanyView import *
from .Views.CustomerView import *

urlpatterns = [
    ###################################
    #            Campaign             #
    ###################################
    path("", GetCampaign.as_view(), name="campaign_fetch"),
    path("detail/", GetCampaignDetail.as_view(), name="campaign_detail"),
    path("create/", CreateCampaign.as_view(), name="campaign_create"),
    path("add/", AddToCampaign.as_view(), name="campaign_add"),
    ###################################
    #            Customer             #
    ###################################
    path("customer/", GetCustomers.as_view(), name="customers_fetch"),
    path("customer/create/", CreateCustomers.as_view(), name="customers_create"),
    path("customer_template/", FetchTemplate.as_view(), name="campaign_create"),
    ###################################
    #            Template             #
    ###################################
    path("template/", GetTemplate.as_view(), name="campaign_create"),
    path('template/add/<int:pk>/', AddTemplate.as_view(), name='template_add'),
    path('template/create/', CreateTemplate.as_view(), name='template_create'),
    path('template/delete/<int:pk>/', DeleteTemplate.as_view(), name='template_delete'),
    path('template/update/<int:pk>/', UpdateTemplate.as_view(), name='template_update'),
    ###################################
    #            Company              #
    ###################################
    path('company/',CompanyListCreate.as_view(),name="company_create_list"),
    path('company/<int:id>/',CompanyDetail.as_view(),name="company_detail_destroy_update"),
    path('generate_messages/',GetMessageFromTemplate.as_view(),name="generate_messages"),
]
