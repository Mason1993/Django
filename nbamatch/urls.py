from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from nbamatch.models import Post
from nbamatch import views

urlpatterns = patterns('',
   
    url(r'^$', views.input),
    url(r'^result/', views.result),

    url(r'^home', ListView.as_view(
	                    queryset = Post.objects.all().order_by("-date")[:10],
	                            template_name = "index.html")),

	                    url(r'^(?P<pk>\d+)$', DetailView.as_view(
	                  	   model = Post,
	                       template_name = "post.html")),

	                    url(r'^newslist/$', ListView.as_view(
	                  	   model = Post,
	                       template_name = "posttitleslist.html")),
	                  
	                    url(r'^contact/$', ListView.as_view(
	                  	   queryset = Post.objects.all().order_by("-date")[:3],
	                       template_name = "contact.html")),
)