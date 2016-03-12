# pystagram/middlewares.py


class SampleMiddleware(object):
    def process_request(self, request):
        request.just_say = 'Hello world'

