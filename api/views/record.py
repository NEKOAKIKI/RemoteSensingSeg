from django.views import View
from django.http import JsonResponse
from app01.models import Record


class RecordDelView(View):
    def delete(self, request):
        res = {
            'code': 201,
            'msg': '删除成功！'
        }
        nid = request.data.get('nid')
        user_query = Record.objects.filter(nid=nid)
        user_query.delete()
        res['code'] = 200
        return JsonResponse(res)