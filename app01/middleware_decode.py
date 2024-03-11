from django.utils.deprecation import MiddlewareMixin
import json


class Md1(MiddlewareMixin):
    def process_request(self, request):
        if request.method != 'GET' and request.META.get('CONTENT_TYPE') == 'application/json':
            data = json.loads(request.body)
            request.data = data

    def process_response(self, request, response):
        return response
