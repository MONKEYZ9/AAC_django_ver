from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.decorator import profile_ownership_required
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    # 이걸 detail로 가고 싶다면 설정해줘야 해 내부 메소드를 수정해서
    # success_url = reverse_lazy('accountapp:hello world')
    template_name = 'profileapp/create.html'


    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk' : self.object.user.pk})
    
    #  form_valid를 불러서
    # 커스터마이징을 해서 다시 보내자
    def form_valid(self, form):
        # form을 받은게 실제 db에 저장하지 않고
        temp_profile = form.save(commit=False)
        # 유저를 가져와서 유저에 담아
        temp_profile.user = self.request.user
        # 저장하기
        temp_profile.save()
        return super().form_valid(form)

@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    # 이거도 해주자
    # success_url = reverse_lazy('accountapp:hello world')
    template_name = 'profileapp/update.html'


    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.user.pk})