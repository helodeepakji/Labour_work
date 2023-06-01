from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def signin(request):
    print(request.POST)
    return JsonResponse({'message': 'Form submitted successfully'})


def signup(request):
    print(request.POST)
    return JsonResponse({'message': 'Form submitted successfully'})

def contact(request):
    print(request.POST)
    return JsonResponse({'message': 'Form submitted successfully'})