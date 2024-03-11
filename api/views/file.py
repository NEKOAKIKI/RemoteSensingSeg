from django.views import View
from django.http import JsonResponse
from app01.models import Avatars, Record
from api.views.detect import main


class FileView(View):
    def post(self, request):
        res = {
            'code': 200,
            'msg': 'success',
            'data': ''
        }
        file = request.FILES.get('file')
        image = Avatars.objects.create(url=file)
        image_path = str(image.url.url)[1:]
        result = main(image_path)
        Record.objects.create(avatars_id=image.nid, user=request.user, result_url=result)
        res['data'] = result
        return JsonResponse(res)
