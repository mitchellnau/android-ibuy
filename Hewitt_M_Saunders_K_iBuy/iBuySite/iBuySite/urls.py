"""iBuySite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', 'iBuySite.views.home', name='home'),


    #url(r'^/register', 'iBuySite.views.home', name='register'),
    #url(r'^/login',    'iBuySite.views.home', name='login'),

    #url(r'^/lists', 'iBuySite.views.home', name='lists'),
    #url(r'^/list_items/(?P<list_id>\w+)/$', 'iBuySite.views.list_items', name='list_items'),
    #url(r'^/list_users/(?P<list_id>\w+)/$', 'iBuySite.views.list_users', name='list_users'),

    #url(r'add_list$', 'iBuySite.views.add_list', name='add_list'),
    #url(r'edit_list/(?P<list_id>\w+)/$', 'iBuySite.views.edit_list', name='edit_list'),
    #url(r'remove_list/(?P<list_id>\w+)/$', 'iBuySite.views.remove_list', name='remove_list'),

    #url(r'list/(?P<list_id>\w+)/add_user$', 'iBuySite.views.add_user', name='add_user'),
    #url(r'list/(?P<list_id>\w+)/remove_user/$', 'iBuySite.views.remove_user', name='remove_user'),

    #url(r'list_items/(?P<list_id>\w+)/add_item$', 'iBuySite.views.add_item', name='add_item'),
    #url(r'list_items/(?P<list_id>\w+)/edit_item/(?P<item_id>\w+)/$', 'iBuySite.views.edit_item', name='edit_item'),
    #url(r'list_items/(?P<list_id>\w+)/remove_item/(?P<item_id>\w+)/$', 'iBuySite.views.remove_item', name='remove_item'),
]
