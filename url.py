from django.urls import path, include
from . import views
#from rest_framework import routers

#router = routers.DefaultRouter()
#router.register('organization', views.organizationView)

from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [ 
#path('', include(router.url))
path('synerd/', views.SynerdList.as_view(), name='SynerdList'),
]

urlpatterns = format_suffix_patterns(urlpatterns)