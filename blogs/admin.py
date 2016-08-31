from django.contrib import admin

# Register your models here.
from blogs.models import Topic, BlogPost

admin.site.register(Topic)
admin.site.register(BlogPost)