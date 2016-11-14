#page rendering and redirecting
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse

#user authentication
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

#cross-site request forgery
from django.template.context_processors import csrf

#models
from iBuySite.models import UserForm

def home(request):
	return render(request, 'index.htm', {})

def register(request):
        if request.method == 'POST':
                form = UserForm(data=request.POST)
                if form.is_valid():
                    user = form.save()
                    return HttpResponseRedirect("../login/")
                else:
                    print(form.errors)
        else:
                form = UserForm()
        return render(request,
                      'register.htm',
                      {'form': form})