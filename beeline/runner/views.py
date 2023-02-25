from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .serializers import AlgorithmResultSerializer
from rest_framework.permissions import IsAuthenticated


@api_view(['POST', 'GET'])
# @authentication_classes(...)
@permission_classes([IsAuthenticated])
def run_algorithm(request):
    """
    Run request algorithm
    """
    if request.method == 'GET':
        return Response('success!!!')
    if request.method == 'POST':
        serializer = AlgorithmResultSerializer(data=request.data)
        if serializer.is_valid():
            # TODO: send request to containerssh to run algo
            # TODO: implement a many to many relation between pairwise gene results and algorithm results object
            # serializer.save()
            return Response(serializer.data, status=status.HTTP_200_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
