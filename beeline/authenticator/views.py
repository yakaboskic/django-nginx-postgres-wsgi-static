from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


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
