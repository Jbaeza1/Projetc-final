from django.contrib import admin
from .models import Organization
from .models import Userinfo
from .models import SubcriptionType
from .models import Service
from .models import Subscriber
from .models import OrganizationMember
from .models import Office
from .models import Officer
from .models import TransferredSubscription

#admin.site.register(Organization)
#admin.site.register(Userinfo)
#admin.site.register(SubcriptionType)
#admin.site.register(Service)
#admin.site.register(Subscriber)
#admin.site.register(OrganizationMember)
#admin.site.register(Office)
#admin.site.register(Officer)
#admin.site.register(TransferredSubscription)

admin.site.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
	list_display = ['__all__'] 

admin.site.register(Userinfo)
class UserinfoAdmin(admin.ModelAdmin):
	list_display = ['__all__'] 

admin.site.register(SubcriptionType)
class SubcriptionTypeAdmin(admin.ModelAdmin):
	list_display = ['__all__'] 

admin.site.register(Service)
class ServiceAdmin(admin.ModelAdmin):
	list_display = ['__all__'] 

admin.site.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
	list_display = ['__all__'] 

admin.site.register(OrganizationMember)
class OrganizationMemberAdmin(admin.ModelAdmin):
	list_display = ['__all__'] 

admin.site.register(Office)
class OfficeAdmin(admin.ModelAdmin):
	list_display = ['__all__'] 

admin.site.register(Officer)
class OfficerAdmin(admin.ModelAdmin):
	list_display = ['__all__'] 

admin.site.register(TransferredSubscription)
class TransferredSubscriptionAdmin(admin.ModelAdmin):
	list_display = ['__all__'] 