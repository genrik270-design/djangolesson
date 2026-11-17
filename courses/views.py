from django.http import HttpResponse
from django.shortcuts import render

def courses_list(request):
    return HttpResponse('Список курсов')
