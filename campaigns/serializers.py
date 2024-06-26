from rest_framework import serializers
from .models import *
import re

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
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
            validated_data['greeting']=re.sub(r'%(\w+)%', r'{{ \1 }}', validated_data.pop('greeting'))
            validated_data['body']=re.sub(r'%(\w+)%', r'{{ \1 }}', validated_data.pop('body'))
            validated_data['ending']=re.sub(r'%(\w+)%', r'{{ \1 }}', validated_data.pop('ending'))
            template= Template.objects.create(**validated_data)
            return template
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['date'] = instance.date.strftime('%Y-%m-%d')
        return representation


class CampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = '__all__'
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['date'] = instance.date.strftime('%Y-%m-%d')
        representation['status'] = representation['status'].capitalize() if representation['status'] else ''
        audience_count = CampaignCustomers.objects.filter(campaign_id=representation['id']).count() if representation['id'] else 0
        representation['audience'] = audience_count
        return representation

class CampaignCustomersSerializer(serializers.ModelSerializer):
    campaign_id = serializers.IntegerField()
    customer_ids = serializers.ListField()

    class Meta:
        model = CampaignCustomers
        fields = '__all__'