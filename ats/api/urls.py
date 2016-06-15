from django.conf.urls import url, include
from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register('Term', views.TermViewSet)


urlpatterns = [
	url(r'^school/$', views.SchoolListView.as_view(), name = 'school_list'),
	url(r'^school/(?P<pk>\d+)/$', views.SchoolDetailView.as_view(), name='school_detail'),
	url(r'^term/$', views.TermListView.as_view(), name = 'term_list'),
	url(r'^term/(?P<pk>\d+)/$', views.TermDetailView.as_view(), name='term_detail'),
	url(r'^', include(router.urls)),
]

