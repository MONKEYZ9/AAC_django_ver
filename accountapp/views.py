from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

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