from django.db import models
from django.contrib.auth.models import User
from django import forms


##################################User##################################
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    username = models.CharField(max_length = 30)
    password = models.CharField(max_length = 30)

    def __unicode__(self):
        return self.user.username
    def getusername(self):
        return self.username

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'password')


##################################List##################################
class List(models.Model):
    title = models.CharField(max_length = 120)
    user = models.ForeignKey(UserProfile)

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('title', 'user')


##################################Item##################################
class Item(models.Model):
    title = models.CharField(max_length = 120)
    quantity = models.IntegerField()
    flock = models.CharField(max_length = 32)

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('title', 'content', 'quantity')


##################################Bridge Tables##################################
class BridgeItemUser(models.Model):
    item = models.ForeignKey(Item)
    user = models.ForeignKey(UserProfile)

class BridgeListUser(models.Model):
    list = models.ForeignKey(List)
    user = models.ForeignKey(UserProfile)