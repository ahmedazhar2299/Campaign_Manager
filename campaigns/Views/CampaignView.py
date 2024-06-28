from campaigns.serializers import CampaignSerializer
from campaigns.models import Campaign, CampaignCustomers, Customer, Template
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q, F


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
    
class GetCampaignDetail(APIView):
    def get(self, request, *args, **kwargs):
        campaign_id = request.GET.get('campaign_id', 0)
        response = {
            "success": False,
            "message": "No data found",
            "data" : {}
        }
        if campaign_id:
            template_data = Campaign.objects.filter(id=campaign_id) \
            .annotate(title=F('template__title'), greeting=F('template__greeting'), body=F('template__body'), ending=F('template__ending')) \
            .values('title', 'greeting', 'body', 'ending').first()

            customer_data = Customer.objects.filter(campaign_customer__campaign_id=campaign_id).values('id', 'first_name', 'last_name')
            
            if template_data or customer_data:
                response = {
                "success": True,
                "message": "Add to Campaign success",
                'data': {
                    'template' : template_data,
                    'customers' : customer_data 
                }
                }
            
        return Response(response)
    
class CreateCampaign(generics.ListCreateAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer

    def get(self, request, *args, **kwargs):
        return Response({"message": "Method not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
class AddToCampaign(APIView):

    def post(self, request, *args, **kwargs):
        campaign_id = request.POST.get('campaign_id', 0)
        template_id = request.POST.get('template_id', 0)
        customer_ids = list(map(int,request.POST.getlist('customer_ids', [])))
        response_data = {"success": False, "message": "Campaign add failure"}

        if campaign_id and customer_ids:
            existing_list = set(CampaignCustomers.objects.filter(campaign_id=campaign_id, customer_id__in=customer_ids).values_list('customer_id', flat=True))
            customer_ids = set(customer_ids).difference(existing_list)
            campaign_customers = [CampaignCustomers(campaign_id=campaign_id, customer_id=id) for id in customer_ids]
            if campaign_customers:
                CampaignCustomers.objects.bulk_create(campaign_customers, batch_size=1000)
                response_data["message"] ="Add to Campaign success"
                response_data["success"] = True
            else:
                response_data["message"] = "Customer Already exists"
        elif campaign_id and template_id:
            template = Template.objects.filter(id=template_id, campaign_id__isnull=True).first()
            if template:
                template.campaign_id = campaign_id
                template.save()
                response_data["success"] = True
                response_data["message"] = "Add to Campaign success"
            else:
                response_data["message"] = "Template already added to campaign"
                

            
        return Response(response_data)