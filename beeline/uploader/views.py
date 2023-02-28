from rest_framework import viewsets

from .models import Dataset, ReferenceNetwork
from .serializers import DatasetSerializer, ReferenceNetworkSerializer


class DatasetViewSet(viewsets.ModelViewSet):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer

class RefNetworkViewSet(viewsets.ModelViewSet):
    queryset = ReferenceNetwork.objects.all()
    serializer_class = ReferenceNetworkSerializer
