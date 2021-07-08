from django.shortcuts import render

# Create your views here.
def hello_world(req):
    if req.method == 'POST':
        return render(req, 'accountapp/hello_world.html',
                      context={'tttt' : 'POST METHOD'})
    else:
        return render(req, 'accountapp/hello_world.html',
                      context={'tttt': 'GET METHOD'})