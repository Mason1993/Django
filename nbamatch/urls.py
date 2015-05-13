from django.conf.urls import patterns, include, url
from nbamatch import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mlproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index),
    url(r'^result/', views.result),
)