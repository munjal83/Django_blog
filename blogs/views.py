from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

from .models import Topic, Blogpost
from .forms import TopicForm, BlogpostForm
# Create your views here.
def index(request):
	"""The home page for Blog"""
	return render(request, 'blogs/index.html')

@login_required
def topics(request):
	"""Show all topics"""
	topics = Topic.objects.filter(owner=request.user).order_by('date_added')
	context = {'topics': topics}
	return render(request, 'blogs/topics.html', context)

@login_required
def topic(request, topic_id):
	"""Show a single topic and all its blog entries"""
	topic = Topic.objects.get(id=topic_id)
	# Make sure the topic belongs to the current user.
	if topic.owner != request.user:
		raise Http404

	blogposts = topic.blogpost_set.order_by('-date_added')
	context = {'topic': topic, 'blogposts': blogposts}
	return render(request, 'blogs/topic.html', context)

@login_required
def new_topic(request):
	"""Add a new topic"""
	if request.method != 'POST':
		# No data submitted; create a blank form.
		form = TopicForm()
	else:
		# POST data submitted; process data
		form = TopicForm(request.POST)
		if form.is_valid():
			new_topic = form.save(commit=False)
			new_topic.owner = request.user
			new_topic.save()
			return HttpResponseRedirect(reverse('blogs:topics'))

	context = {'form': form}
	return render(request, 'blogs/new_topic.html', context)

@login_required
def new_blogpost(request, topic_id):
	"""Add a new blogpost for a particular topic"""
	topic = Topic.objects.get(id=topic_id)

	if request.method != 'POST':
		# No data submitted; create a blank form.
		form = BlogpostForm()
	else:
		# POST data submitted; process data.
		form =  BlogpostForm(data=request.POST)
		if form.is_valid():
			new_blogpost = form.save(commit=False)
			if new_blogpost.owner == request.user:
				new_blogpost.topic = topic
				new_blogpost.save()
			return HttpResponseRedirect(reverse('blogs:topic', args=[topic_id]))
	context = {'topic': topic, 'form': form}
	return render(request, 'blogs/new_blogpost.html', context)

@login_required
def edit_blogpost(request, blogpost_id):
	"""Edit an existing blogpost."""
	blogpost = Blogpost.objects.get(id=blogpost_id)
	topic = blogpost.topic
	if topic.owner != request.user:
		raise Http404

	if request.method != 'POST':
		# Initial request; pre-fill form with the current entry.
		form = BlogpostForm(instance=blogpost)
	else:
		# POST data submitted; process data.
		form = BlogpostForm(instance=blogpost, data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('blogs:topic',args=[topic.id]))
	context = {'blogpost': blogpost, 'topic': topic, 'form': form}
	return render(request, 'blogs/edit_blogpost.html', context)


	