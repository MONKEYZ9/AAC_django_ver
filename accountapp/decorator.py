from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


def account_ownership_required(func):
    def decorated(req, *args, **kwargs):
        # 요청한 유저 오브젝스의 pk값을 확인
        user = User.objects.get(pk=kwargs['pk'])
        if not user == req.user:
            return HttpResponseForbidden()
        return func(req, *args, **kwargs)

    return decorated
