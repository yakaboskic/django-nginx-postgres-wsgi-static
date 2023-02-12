from rest_framework import serializers
from .models import AlgorithmResult

class AlgorithmResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = AlgorithmResult
        fields = ['created', 'algorithm', 'owner', 'dataset']