from django.contrib import admin
from iBuySite.models import UserProfile, List, Item, BridgeItemUser, BridgeListUser

# Register your models here.
#class SeatsAdmin(admin.ModelSeats):
#	pass
#	admin.site.register(Seats, SeatsAdmin)


admin.site.register(UserProfile)
admin.site.register(List)
admin.site.register(Item)
admin.site.register(BridgeItemUser)
admin.site.register(BridgeListUser)