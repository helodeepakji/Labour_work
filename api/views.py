from django.http import JsonResponse
from django.shortcuts import render
from .serializers import *
from .utils import convert_gender
import json
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

# Create your views here.
def signin(request):
    print(request.POST)
    return JsonResponse({'message': 'Form submitted successfully'})


def signup(request):
    print(request.POST)
    if request.POST.get('gender',None) != None:
        temp_gender = convert_gender(request.POST['gender'])
    else:
        temp_gender = None
    temp_auth = {
        'username': request.POST['phone'],
        'Name': request.POST['name'],
        'Gender':temp_gender,
        'Is_worker': True,
        'Is_customer': False,
        'password': request.POST['password'],
        'cpassword':request.POST['cpassword']
    }
    print('temp auth',temp_auth)
    register_serializer = RegisterAuthSerializer(data=temp_auth)
    register_serializer.is_valid(raise_exception=True)
    register_serializer.save()
    token_serializer = MyTokenObtainPairSerializer(data=temp_auth)
    tokens = token_serializer.get_token(register_serializer.instance)
    access_token = tokens.access_token
    print('tokens',tokens)
    return JsonResponse({'message': 'User created successfully','tokens':{'access':str(access_token),'refresh':str(tokens)}})

class loginView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class TokenRefreshView(TokenRefreshView):
    serializer_class = MyTokenObtainPairSerializer

def contact(request):
    print(request.POST)
    return JsonResponse({'message': 'Form submitted successfully'})