from rest_framework.serializers import Serializer, FileField
from .models import AlgorithmResult

class AlgorithmResultSerializer(serializers.ModelSerializer):
    file = serializers.FileField(required=False, allow_empty_file=True)

    class Meta:
        model = AlgorithmResult
        fields = ['created', 'algorithm', 'owner', 'dataset', 'file']

class UploadSerializer(Serializer):
    file_uploaded = FileField()
   
    class Meta:
        fields = ['file_uploaded']
