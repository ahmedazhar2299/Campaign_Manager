
from campaigns.serializers import TemplateSerializer, CampaignSerializer
from campaigns.models import CampaignCustomers, Template, Campaign, Customer
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from ..utils import render_text_template

class FetchTemplate(APIView):
    """
    API view to fetch template against a customer
    """
    def get(self, request, *args, **kwargs):
        campaign_id = int(request.GET.get('campaign_id', 0))
        customer_id = int(request.GET.get('customer_id', 0))

        if campaign_id and customer_id:
            template = Campaign.objects.filter(id=campaign_id).values_list('template__content',flat=True).first()
            customer = Customer.objects.filter(id=customer_id).first()
            if template and customer:
                context={
                    'first_name':customer.first_name,
                    'last_name':customer.last_name,
                    'company':customer.company
                }
                template_content=render_text_template(template,context)
                return Response({"success": True,"message": "Template Retrieved Successfully!", 'data': {'template_content': template_content}}, status=status.HTTP_200_OK)

        return Response({"success": False,"message": "Invalid Parmas"}, status=status.HTTP_404_NOT_FOUND)


class CreateTemplate(generics.ListCreateAPIView):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer

    def get(self, request, *args, **kwargs):
        return Response({"message": "Method not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class AddTemplate(generics.RetrieveUpdateAPIView):
    """
    Request Method : PUT, PATCH
    """
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer

    def get(self, request, *args, **kwargs):
        return Response({"message": "Method not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    

class DeleteTemplate(generics.DestroyAPIView):
    """
    Request Method : Delete
    """
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer

    def get(self, request, *args, **kwargs):
        return Response({"message": "Method not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    
    
class UpdateTemplate(generics.RetrieveUpdateAPIView):
    """
    Request Method : PUT, PATCH
    """
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer

    def get(self, request, *args, **kwargs):
        return Response({"message": "Method not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class GetMessageFromTemplate(APIView):
    def get(self,request,*args,**kwargs):
        try:
            campaign_id=request.query_params.get('campaign_id',None)
            if campaign_id is None:
                return Response({"error":" Campaign id are required"})
            campaign = Campaign.objects.filter(id=campaign_id).first()
            campaign_customers=CampaignCustomers.objects.filter(campaign=campaign)

            messages=[]
            for customer in campaign_customers.all():
                context={
                    'first_name':customer.customer.first_name,
                    'last_name':customer.customer.last_name,
                    'company':customer.customer.company
                }
                message=render_text_template(campaign.template.content,context)
                messages.append(message)

            return Response({"success":"true","message":"All Customers Message Generated Successfully","data":{'content':messages}},status=200)
        except Exception as e:
            error=str(e)
            print(error)
            return Response({"error":f"Unexpected error {error}"},status=400)

