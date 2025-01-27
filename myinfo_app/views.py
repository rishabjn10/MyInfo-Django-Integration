from rest_framework.decorators import api_view
from rest_framework.response import Response
from myinfo_app.client import MyInfoPersonalClientV4
from django.utils.crypto import get_random_string

CLIENT = MyInfoPersonalClientV4()
CALLBACK_URL = "http://localhost:3001/callback"

oauth_state = get_random_string(length=16)

@api_view(['GET'])
def auth_login(request):
    auth_url = CLIENT.get_authorise_url(oauth_state, CALLBACK_URL)
    return Response({'auth_url': auth_url})

@api_view(['GET'])
def auth_callback(request):
    auth_code = request.GET.get('code')
    if not auth_code:
        return Response({'error': 'Authorization code missing'}, status=400)

    person_data = CLIENT.retrieve_resource(auth_code, oauth_state, CALLBACK_URL)
    return Response(person_data)
