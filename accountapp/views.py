from django.http import HttpResponse
from django.shortcuts import render

from accountapp.models import HelloWorld


# Create your views here.


def hello_world(request):
    if request.method == "POST":
        temp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()
        new_hello_world.text = temp
        new_hello_world.save() # DB에 HelloWorld 객체 저장

        return render(request, 'accountapp/hello_world.html', context={'hello_world_output': new_hello_world})
    return render(request, 'accountapp/hello_world.html', context={'text': 'GET METHOD!!!'})
