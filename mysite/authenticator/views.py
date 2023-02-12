from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .serializers import AlgorithmResultSerializer
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


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

@csrf_exempt
def password_auth(request):
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        remote_address = data.get('remoteAddress')
        connection_id = data.get('connectionId')
        password_base64 = data.get('passwordBase64')

        # TODO:V erify user and password 

        return JsonResponse({'success': True})
    return JsonResponse({'success': False})

@csrf_exempt
def pubkey_auth(request):
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        remote_address = data.get('remoteAddress')
        connection_id = data.get('connectionId')
        public_key = data.get('publicKey')

        # TODO: Verify user and password 

        return JsonResponse({'success': True})
    return JsonResponse({'success': False})