from campaigns.serializers import CampaignSerializer, CampaignCustomersSerializer
from campaigns.models import Campaign, CampaignCustomers
from rest_framework import generics, status
from rest_framework.views import APIView
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
        search_term = self.request.query_params.get('search_term', '')
        from_template = bool(self.request.query_params.get('from_template', False))

        q_obj = Q()
        if search_term:
            q_obj &= (Q(name__icontains=search_term) | Q(status__icontains=search_term))
        if from_template:
            q_obj &= Q(template__isnull=True)

        queryset = queryset.filter(q_obj)
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
    
class AddToCampaign(APIView):

    def post(self, request, *args, **kwargs):
        campaign_id = request.POST.get('campaign_id', 0)
        customer_ids = list(map(int,request.POST.getlist('customer_ids', [])))
        response_data = {"success": False, "message": "Add to Campaign failure"}

        if campaign_id and customer_ids:
            existing_list = set(CampaignCustomers.objects.filter(campaign_id=campaign_id, customer_id__in=customer_ids).values_list('customer_id', flat=True))
            customer_ids = set(customer_ids).difference(existing_list)
            print('print(existing_list)', existing_list)
            print('print(customer_ids)', customer_ids)
            campaign_customers = [CampaignCustomers(campaign_id=campaign_id, customer_id=id) for id in customer_ids]
            if campaign_customers:
                CampaignCustomers.objects.bulk_create(campaign_customers, batch_size=1000)
                response_data = {
                "success": True,
                "message": "Add to Campaign success"
                }
            else:
                response_data = {
                "success": False,
                "message": "Customer Already exists"
                }

            
        return Response(response_data)