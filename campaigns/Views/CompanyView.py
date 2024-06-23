from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from ..models import Company
from ..serializers import CompanySerializer


class CompanyListCreate(ListCreateAPIView):
    serializer_class=CompanySerializer
    queryset=Company.objects.all()

class CompanyDetail(RetrieveUpdateDestroyAPIView):
    serializer_class=CompanySerializer
    lookup_field='id'
    queryset=Company.objects.all()

