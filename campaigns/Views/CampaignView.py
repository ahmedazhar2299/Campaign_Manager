from campaigns.serializers import CampaignSerializer, CustomerSerializer
from campaigns.models import Campaign, Customer
from rest_framework import generics, status
from rest_framework.response import Response

"""
Using generic views in Django REST framework for this project for quickly setting up basic CRUD operations /
without writing repetitive code, ensuring our APIs are easier to maintain. 
"""


class CreateCampaign(generics.ListCreateAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer

    def get(self, request, *args, **kwargs):
        return Response({"message": "Method not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class AddCustomers(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
