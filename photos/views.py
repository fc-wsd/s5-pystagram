import logging

from django.contrib import messages
from django.shortcuts import render
from django.shortcuts import get_object_or_404
#from django.http import HttpResponse

#from pystagram.middlewares import HelloWorldError
from .models import Photo


logger = logging.getLogger('django')


def toppage(request):
    messages.info(request, '글 목록에 접근하셨습니다.')
    logger.warning('the toppage view is called')
    #raise HelloWorldError('으악 뭔가 이상해')
    #return HttpResponse('hello world')

    photos = Photo.objects.order_by('-updated_at')
    ctx = {
        'object_list': photos,
    }

    return render(request, 'toppage.html', ctx)


def view_photo(request, pk):
    photo = get_object_or_404(Photo, pk=pk)
    ctx = {
            'photo': photo,
    }
    return render(request, 'view_photo.html', ctx)

