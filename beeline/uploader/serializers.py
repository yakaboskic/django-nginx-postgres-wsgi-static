from rest_framework import serializers
from .models import Dataset

class DatasetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Dataset
        fields = ['owner', 'file', 'upload_at']
