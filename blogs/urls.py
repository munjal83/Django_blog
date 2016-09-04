"""Define URL patterns for blogs"""

from django.conf.urls import url

from . import views

urlpatterns = [
	#Home Page
	url(r'^$', views.index, name='index'),
]