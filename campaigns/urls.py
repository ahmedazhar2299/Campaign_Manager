from django.urls import path

from .Views.CampaignView import *
from .Views.TemplateView import *
from .Views.CompanyView import *

urlpatterns = [
    path("create/", CreateCampaign.as_view(), name="campaign_create"),
    path("customers/", AddCustomers.as_view(), name="campaign_create"),
    path("template/", FetchTemplate.as_view(), name="campaign_create"),
    path('template/add/<int:pk>/', AddTemplate.as_view(), name='template_add'),
    path('template/create/', CreateTemplate.as_view(), name='template_create'),
    path('template/delete/<int:pk>/', DeleteTemplate.as_view(), name='template_delete'),
    path('template/update/<int:pk>/', UpdateTemplate.as_view(), name='template_update'),
    path('company/',CompanyListCreate.as_view(),name="company_create_list"),
    path('company/<int:id>/',CompanyDetail.as_view(),name="company_detail_destroy_update"),
]
