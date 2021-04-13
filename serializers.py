from rest_framework import serializers
from .models import Organization
from .models import Userinfo
from .models import SubcriptionType
from .models import Service
from .models import Subscriber
from .models import OrganizationMember
from .models import Office
from .models import Officer
from .models import TransferredSubscription

class OrganizationSerializer (serializers.ModelSerializer):

	class Meta:
		model = Organization
#		fields = ('Organizationcode','name','description','date_joined','address1','address2','city','state','zipcode','phone_number')
		fields = '__all__'

class UserinfoSerializer (serializers.ModelSerializer):

	class Meta:
		model = Userinfo
		fields = '__all__'

class SubcriptionTypeSerializer (serializers.ModelSerializer):

	class Meta:
		model = SubcriptionType
		fields = '__all__'

class ServiceSerializer (serializers.ModelSerializer):

	class Meta:
		model = Service
		fields = '__all__'

class SubscriberSerializer (serializers.ModelSerializer):

	class Meta:
		model = Subscriber
		fields = '__all__'

class OrganizationMemberSerializer (serializers.ModelSerializer):

	class Meta:
		model = OrganizationMember
		fields = '__all__'

class OfficeSerializer (serializers.ModelSerializer):

	class Meta:
		model = Office
		fields = '__all__'

class OfficerSerializer (serializers.ModelSerializer):

	class Meta:
		model = Officer
		fields = '__all__'

class TransferredSubscriptionSerializer (serializers.ModelSerializer):

	class Meta:
		model = TransferredSubscription
		fields = '__all__'