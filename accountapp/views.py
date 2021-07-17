from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.decorator import account_ownership_required
from accountapp.forms import AccountUpdateForm
from accountapp.models import HelloWorld

# 코드 줄이기
has_ownership = [login_required, account_ownership_required]


@login_required
def hello_world(req):
    if req.method == 'POST':

        temp = req.POST.get('input_text')
        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save()

        return HttpResponseRedirect(reverse('accountapp:hello world'))

    else:
        new_hello_world_list = HelloWorld.objects.all()

        return render(req, 'accountapp/hello_world.html',
                      context={'new_hello_world_list': new_hello_world_list})


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello world')
    template_name = 'accountapp/create.html'


class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'


# 회원정보 업데이트
@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User  # class AbstractUser(AbstractBaseUser, PermissionsMixin): 여기 함 들어가서 어떻게 되있나 봐봐라
    context_object_name = 'target_user'
    form_class = AccountUpdateForm  # 새롭게 만든 폼.py를 만들어서 옮겼어
    success_url = reverse_lazy('accountapp:hello world')
    template_name = 'accountapp/update.html'
    
    # 본인인지 확인 하는 것은 커스텀 데코


# 탈퇴
@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'

    # 본인인지 확인 하는 것은 커스텀 데코

