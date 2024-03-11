from django.views import View
from django.http import JsonResponse
from app01.models import UserInfo


class UserLurView(View):
    def delete(self, request):
        res = {
            'code': 201,
            'msg': '删除成功！'
        }
        nid = request.data.get('nid')
        user_query = UserInfo.objects.filter(nid=nid)
        user_query.delete()
        res['code'] = 200
        return JsonResponse(res)

    def put(self, request):
        res = {
            'code': 201,
            'msg': '修改成功！'
        }
        nid = request.data.get('nid')
        user_name = request.data.get('userName')
        user_sex = request.data.get('userSex')
        age = request.data.get('age')
        phone = request.data.get('phone')
        user_query = UserInfo.objects.filter(nid=nid)
        user_query.update(name=user_name, sex=user_sex, age=age, tel=phone)
        res['code'] = 200
        return JsonResponse(res)
