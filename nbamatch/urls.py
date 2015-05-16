from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from nbamatch.models import Post
from nbamatch import views

urlpatterns = patterns('',
    
	url(r'^$', ListView.as_view(
	                    queryset = Post.objects.all().order_by("-date")[:10],
	                    template_name = "index.html"), 
	                    name='index'),
	url(r'^input/$', views.input),
	url(r'^input/c/$', views.inputc),

	url(r'^input/c/result/$', views.resultc),   
)