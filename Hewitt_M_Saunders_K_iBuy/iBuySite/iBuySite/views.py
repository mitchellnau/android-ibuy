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
from iBuySite.models import UserProfile, List, Item, BridgeItemUser, BridgeListUser

def home(request):
	return render(request, 'index.htm', {})