from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
import datetime

import django.contrib.auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.contrib.auth import authenticate
from django.core.urlresolvers import reverse

from LezTurn_Account.forms import LoginForm, RegisterForm
from LezTurn_Core.models import LezUser

def mainpage(request):
    return HttpResponse("Hello World")

def login(request):
    if request.method == 'GET':
        form = LoginForm()
        
        return render_to_response('login.html', {'form':form},
                                  context_instance=RequestContext(request))

    if request.method == 'POST':
        
        form = LoginForm(request.POST)
        if not form.is_valid():
            return render_to_response('login.html', {'form':form},
                                  context_instance=RequestContext(request))

        user = authenticate(username=request.POST['username'],
                            password=request.POST['password'])
        if user is None:
            return render_to_response('login.html',
                                      {'form':form,
                                       'error': 'Invalid username or password'},
                                      context_instance=RequestContext(request))
        django.contrib.auth.login(request,user)
        return HttpResponseRedirect(reverse('mainpage'))

def logout(request):
    django.contrib.auth.logout(request)
    return HttpResponseRedirect(reverse('list.views.index'))


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            LezUser.objects.create_user(cd['username'],email=cd['email'],password=cd['password'])
            return HttpResponseRedirect(reverse('mainpage'))
        else:
            f = RegisterForm(auto_id=False)
            msg = 'Registration failed...'
            context={'f':f, 'message': msg}
            return render(request, 'register.html', context)
    else:
        f = RegisterForm(auto_id=False)
        context={'f':f}
        return render(request, 'register.html', context)

