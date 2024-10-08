from django.shortcuts import render
from django.http import JsonResponse

def projects_home(request, *args, **kwargs):
    return JsonResponse({"message": "project api response"})