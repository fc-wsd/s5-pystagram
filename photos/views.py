from django.shortcuts import render
from django.http import HttpResponse

from pystagram.middlewares import HelloWorldError


def toppage(request):
    raise HelloWorldError('으악 뭔가 이상해')
    return HttpResponse('hello world')

