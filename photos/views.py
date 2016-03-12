from django.shortcuts import render
from django.http import HttpResponse


def toppage(request):
    return HttpResponse('hello world')

