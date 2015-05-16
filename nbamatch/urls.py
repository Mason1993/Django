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
	url(r'^input/pg/$', views.inputpg),
	url(r'^input/pf/$', views.inputpf),
	url(r'^input/sg/$', views.inputsg),
	url(r'^input/sf/$', views.inputsf),

	url(r'^input/c/result/$', views.resultc),
	url(r'^input/pg/result/$', views.resultpg), 
	url(r'^input/pf/result/$', views.resultpf), 
	url(r'^input/sg/result/$', views.resultsg), 
	url(r'^input/sf/result/$', views.resultsf),    
)