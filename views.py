from django.shortcuts import render

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
#from rest_framework import viewsets


from .models import Organization
from .models import Userinfo
from .models import SubcriptionType
from .models import Service
from .models import Subscriber
from .models import OrganizationMember
from .models import Office
from .models import Officer
from .models import TransferredSubscription

from .serializers import OrganizationSerializer
from .serializers import UserinfoSerializer
from .serializers import SubcriptionTypeSerializer
from .serializers import ServiceSerializer
from .serializers import SubscriberSerializer
from .serializers import OrganizationMemberSerializer
from .serializers import OfficeSerializer
from .serializers import OfficerSerializer
from .serializers import TransferredSubscriptionSerializer

# organization info
# synerd/

#class SynerdList(viewsets.ModelViewSet):
	#queryset = Organization.objects.all()
	#serializer_class = OrganizationSerializer

class SynerdList(APIView):

	def get(self, request):
		organization = Organization.objects.all()
		serializer1 = OrganizationSerializer(organization, many=True)
		return Response(serializer1.data)

		userinfo = Userinfo.objects.all()
		serializer2 = OrganizationSerializer(userinfo, many=True)
		return Response(serializer2.data)

		subcriptionType = SubcriptionType.objects.all()
		serializer3 = OrganizationSerializer(subcriptionType, many=True)
		return Response(serializer3.data)

		service = Service.objects.all()
		serializer4 = OrganizationSerializer(service, many=True)
		return Response(serializer4.data)

		subscriber = Subscriber.objects.all()
		serializer5 = OrganizationSerializer(subscriber, many=True)
		return Response(serializer5.data)

		organizationMember = OrganizationMember.objects.all()
		serializer6 = OrganizationSerializer(organizationMember, many=True)
		return Response(serializer6.data)

		office = Office.objects.all()
		serializer7 = OrganizationSerializer(office, many=True)
		return Response(serializer7.data)

		officer = Officer.objects.all()
		serializer8 = OrganizationSerializer(officer, many=True)
		return Response(serializer8.data)

		transferredSubscription = TransferredSubscription.objects.all()
		serializer9 = OrganizationSerializer(transferredSubscription, many=True)
		return Response(serializer9.data)

	def post(self):
		pass