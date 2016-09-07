"""Define URL patterns for blogs"""

from django.conf.urls import url

from . import views

urlpatterns = [
	# Home Page
	url(r'^$', views.index, name='index'),

	# Show all topics.
	url(r'^topics/$', views.topics, name='topics'),

	# Detail page for a single topic
	url(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'), 

	# Page for adding a new topic
	url(r'^new_topic/$', views.new_topic, name='new_topic'),

	# Page for adding a new blogpost
	url(r'^new_blogpost/(?P<topic_id>\d+)/$', views.new_blogpost, name='new_blogpost'),

	# Page for editing a blogpost
	url(r'^edit_blogpost/(?P<blogpost_id>\d+)/$', views.edit_blogpost, name='edit_blogpost'),
]