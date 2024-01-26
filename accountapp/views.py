from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.forms import UserUpdateForm
from accountapp.models import HelloWorld


# Create your views here.


def hello_world(request):
    if request.method == "POST":
        temp = request.POST.get('hello_world_input')

        if temp:
            new_hello_world = HelloWorld()
            new_hello_world.text = temp
            new_hello_world.save() # DB에 HelloWorld 객체 저장

#        hello_world_list = HelloWorld.objects.all()
#        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})
        return HttpResponseRedirect(reverse('accountapp:hello_world'))
                                                # account 내 있는 hello world로 재접속하라
    hello_world_list = HelloWorld.objects.all()
    return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'

class AccountDetailView (DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = UserUpdateForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'

class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'
