from rest_framework.generics import ListCreateAPIView
from campaigns.serializers import CustomerSerializer
from campaigns.models import Customer
from rest_framework.response import Response
from rest_framework import generics, status
from django.db.models import Q


class GetCustomers(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get_queryset(self):
        queryset = Customer.objects.all()
        search_term = self.request.query_params.get('search_term')
        campaign_id = self.request.query_params.get('campaign_id')
        if search_term:
            queryset = queryset.filter(
                Q(first_name__icontains=search_term) |
                Q(last_name__icontains=search_term)
            
            )
        if campaign_id:
            queryset = queryset.filter(Q(campaign_customer__campaign_id=campaign_id))

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

class CreateCustomers(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def get(self, request, *args, **kwargs):
        return Response({"message": "Method not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)