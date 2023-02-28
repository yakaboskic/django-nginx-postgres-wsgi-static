from rest_framework import serializers
from .models import Dataset, ReferenceNetwork

class DatasetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dataset
        fields = ['pk', 'owner', 'pseudo_time_file', 'expression_data_file', 'ref_network', 'upload_at']

class ReferenceNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferenceNetwork
        fields = ['pk', 'owner', 'file', 'upload_at']
