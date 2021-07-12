from django.shortcuts import render

# Create your views here.
def hello_world(req):
    if req.method == 'POST':

        temp = req.POST.get('input_text')


        return render(req, 'accountapp/hello_world.html',
                      context={'tttt' : temp})
    else:
        return render(req, 'accountapp/hello_world.html',
                      context={'tttt': 'GET METHOD'})