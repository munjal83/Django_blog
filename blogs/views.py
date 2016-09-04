from django.shortcuts import render

from .models import Topic
# Create your views here.
def index(request):
	"""The home page for Blog"""
	return render(request, 'blogs/index.html')

def topics(request):
	"""Show all topics"""
	topics = Topic.objects.order_by('date_added')
	context = {'topics': topics}
	return render(request, 'blogs/topics.html', context)