from campaigns.serializers import CampaignSerializer
from campaigns.models import Campaign
from rest_framework import generics, status
from rest_framework.response import Response
from django.db.models import Q

"""
Using generic views in Django REST framework for this project for quickly setting up basic CRUD operations /
without writing repetitive code, ensuring our APIs are easier to maintain. 
"""

class GetCampaign(generics.ListCreateAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer

    def get_queryset(self):
        queryset = Campaign.objects.all()
        search_term = self.request.query_params.get('search_term')
        if search_term:
            queryset = queryset.filter(
                Q(name__icontains=search_term) |
                Q(status__icontains=search_term)
            )
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data
        response_data = {
            "success": True,
            "message": "Retrieval success",
            "data": data
        }
        return Response(response_data)

    def post(self, request, *args, **kwargs):
        return Response({"message": "Method not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
class CreateCampaign(generics.ListCreateAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer

    def get(self, request, *args, **kwargs):
        return Response({"message": "Method not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

