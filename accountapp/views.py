from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.forms import AccountUpdateForm
from accountapp.models import HelloWorld


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
class AccountUpdateView(UpdateView):
    model = User  # class AbstractUser(AbstractBaseUser, PermissionsMixin): 여기 함 들어가서 어떻게 되있나 봐봐라
    form_class = AccountUpdateForm  # 새롭게 만든 폼.py를 만들어서 옮겼어
    success_url = reverse_lazy('accountapp:hello world')
    template_name = 'accountapp/update.html'


# 탈퇴
class AccountDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'
