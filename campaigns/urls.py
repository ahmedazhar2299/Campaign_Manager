from django.urls import path

from .Views.CampaignView import *
from .Views.TemplateView import *
from .Views.CompanyView import *
from .Views.CustomerView import *

urlpatterns = [
    path("", GetCampaign.as_view(), name="campaign_fetch"),
    path("create/", CreateCampaign.as_view(), name="campaign_create"),
    path("customer/", GetCustomers.as_view(), name="customers_fetch"),
    path("customer/create/", CreateCustomers.as_view(), name="customers_create"),
    path("template/", FetchTemplate.as_view(), name="campaign_create"),
    path('template/add/<int:pk>/', AddTemplate.as_view(), name='template_add'),
    path('template/create/', CreateTemplate.as_view(), name='template_create'),
    path('template/delete/<int:pk>/', DeleteTemplate.as_view(), name='template_delete'),
    path('template/update/<int:pk>/', UpdateTemplate.as_view(), name='template_update'),
    path('company/',CompanyListCreate.as_view(),name="company_create_list"),
    path('company/<int:id>/',CompanyDetail.as_view(),name="company_detail_destroy_update"),
    path('generate_messages/',GetMessageFromTemplate.as_view(),name="generate_messages"),
]
