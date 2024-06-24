from rest_framework import serializers
from .models import *
import re

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['id'] = 'CUST-' + str(representation['id']) if representation['id'] else ''
        representation['created_on'] = instance.created_on.strftime('%Y-%m-%d')
        representation['first_name'] = representation['first_name'].capitalize() if representation['first_name'] else ''
        representation['last_name'] = representation['last_name'].capitalize() if representation['last_name'] else ''
        representation['category'] = representation['category'].capitalize() if representation['category'] else ''
        return representation
    

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
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['id'] = 'CMP-' + str(representation['id']) if representation['id'] else ''
        representation['date'] = instance.date.strftime('%Y-%m-%d')
        representation['status'] = representation['status'].capitalize() if representation['status'] else ''
        return representation

class CampaignCustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampaignCustomers
        fields = '__all__'
