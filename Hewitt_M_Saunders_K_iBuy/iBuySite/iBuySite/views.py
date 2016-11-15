#page rendering and redirecting
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse

#user authentication
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

#cross-site request forgery
from django.template.context_processors import csrf

#models
from iBuySite.models import UserForm, List, ListForm, BridgeListUser

def home(request):
    return render(request, 'index.htm', {})

def register(request):
    if request.method == 'POST':
        form = UserForm(data=request.POST)
        if form.is_valid():
            user = User.objects.create_user(request.POST['username'], email=None, password=request.POST['password'])
            user.save()
            return HttpResponseRedirect("../login/")
        else:
            print(form.errors)
    else:
        form = UserForm()
    return render(request,
                    'register.htm',
                    {'form': form})

def userlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect("../lists/")
        else:
            form = UserForm()
            form.username = username
            return render(request, 'login.htm', {'form': form,
                                                 'error': "Invalid login credentials."})
    else:
        form = UserForm()
        return render(request,
                    'login.htm',
                    {'form': form,
                     'error': ""})

@login_required
def userlogout(request):
    logout(request)
    return render(request, "logout.htm")

@login_required
def get_lists(request):
    owned_lists = List.objects.all().filter(user = request.user)
    membered_lists = BridgeListUser.objects.all().filter(user = request.user)
    lists = owned_lists
    form = ListForm()
    return render(request, 'lists.htm', {'lists' : lists, 'membered_lists' : membered_lists, 'form': form})


@login_required
def add_list(request):
    if request.method == 'POST':
        temp = List()
        temp.title = request.POST['title']
        temp.user = request.user
        temp.save()
        print("List saved.")
        return HttpResponseRedirect("../lists/")
    else:
        return HttpResponseRedirect("../lists/")

@login_required
def remove_list(request, list_id):
    if request.method == 'POST':
        temp = List.objects.get(pk=list_id)
        if request.user == temp.user:
            temp.delete()
        return HttpResponseRedirect("../../lists/")
    else:
        return HttpResponseRedirect("../../lists/")

    