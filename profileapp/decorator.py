from django.http import HttpResponseForbidden

from profileapp.models import Profile


def profile_ownership_required(func):
    def decorated(req, *args, **kwargs):
        # 요청한 유저 오브젝스의 pk값을 확인
        profile = Profile.objects.get(pk=kwargs['pk'])
        if not profile.user == req.user:
            return HttpResponseForbidden()
        return func(req, *args, **kwargs)

    return decorated
