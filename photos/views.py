from django.shortcuts import render
from django.http import HttpResponse


def toppage(request):
    print(request.just_say)
    return HttpResponse('hello world')

