from rest_framework import serializers
from .models import *
import re

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = '__all__'
    def create(self,validated_data):
            template_text=validated_data.pop('content')
            validated_data['content']=re.sub(r'%(\w+)%', r'{{ \1 }}', template_text)
            template= Template.objects.create(**validated_data)
            return template


class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = '__all__'


class CampaignCustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampaignCustomers
        fields = '__all__'
