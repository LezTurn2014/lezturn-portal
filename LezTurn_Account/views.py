from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response
import datetime

import django.contrib.auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.urlresolvers import reverse

from LezTurn_Account.forms import LoginForm

def mainpage(request):
    return HttpResponse("Hello World")

def login(request):
    if request.method == 'GET':
        form = LoginForm()
        next = request.GET['next']
        return render_to_response('login.html', {'form':form,
                                                      'next':next},
                                  context_instance=RequestContext(request))

    if request.method == 'POST':
        next = request.POST['next']
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
        return HttpResponseRedirect(reverse(next))

def logout(request):
    django.contrib.auth.logout(request)
    return HttpResponseRedirect(reverse('list.views.index'))