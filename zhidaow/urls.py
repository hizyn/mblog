from django.conf.urls import patterns, url

from zhidaow import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^column/(?P<pk>\d+)/$', views.column, name='column'),
	url(r'^post/(?P<pk>\d+)$', views.post, name='post'),
	url(r'^tag/(?P<pk>\d+)/$', views.tag, name='tag'),
	url(r'^author/(?P<pk>\d+)/$', views.author, name='author'),
)
