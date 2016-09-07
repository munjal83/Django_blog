from django import forms

from .models import Topic, Blogpost

class TopicForm(forms.ModelForm):
	class Meta:
		model = Topic
		fields = ['text']
		labels = {'text': ''}

class BlogpostForm(forms.ModelForm):
	"""docstring for BlogpostForm"""
	class Meta:
		model = Blogpost
		fields = ['title', 'text']
		labels = {'title': '', 'text': ''} 
		widgets = {'title': forms.TextInput(attrs={'size': 80}), 'text': forms.Textarea(attrs={'cols': 80})}
			
			    
