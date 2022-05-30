from django.urls import path, re_path
from . import views

urlpatterns = [
	re_path(r'^$', views.index, name='index'),
	re_path(r'^comics/$', views.ComicListView.as_view(), name='comics'),
	re_path(r'^comic/(?P<pk>\d+)$', views.ComicDetailView.as_view(), name='comic-detail'),
	re_path(r'^publishers/$', views.PublisherListView.as_view(), name='publishers'),
	re_path(r'^publisher/(?P<pk>\d+)$', views.PublisherDetailView.as_view(), name='publisher-detail'),
]