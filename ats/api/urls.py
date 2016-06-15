from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^school/$', views.SchoolListView.as_view(),
	name = 'school_list'),
	url(r'^school/(?P<pk>\d+)/$', views.SchoolDetailView.as_view(),
		name='school_detail'),
]

