from django.db import models
from django.contrib.auth.models import User
from django import forms


##################################User##################################
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'password')


##################################List##################################
class List(models.Model):
    title = models.CharField(max_length = 120)
    user = models.ForeignKey(User)

class ListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ('title', 'user')


##################################Item##################################
class Item(models.Model):
    title = models.CharField(max_length = 120)
    quantity = models.IntegerField()
    urgency_type = (
        ('1', 'Low'),
        ('2', 'Medium'),
        ('3', 'High'))
    urgency = models.CharField(max_length=1, choices=urgency_type, default='2',
                                    null=True, blank=True)
    category_type = (
        ('1', 'Car'),
        ('2', 'Groceries'),
        ('3', 'Household'))
    category = models.CharField(max_length=1, choices=urgency_type, default='2',
                                    null=True, blank=True)
    cost = models.IntegerField()
    date = models.DateField(auto_now_add=True, blank=True)

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('title', 'quantity', 'urgency', 'cost', 'category')


##################################Bridge Tables##################################
class BridgeItemUser(models.Model):
    item = models.ForeignKey(Item)
    user = models.ForeignKey(User)

class BridgeListUser(models.Model):
    list = models.ForeignKey(List)
    user = models.ForeignKey(User)