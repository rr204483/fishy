from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^myview/$', views.curr_datetime),
    url(r'^schooladd/$', views.create_school, name="schooladd"),
    url(r'^listschools/$', views.list_schools, name="list_schools"),
	url(r'^school/(?P<pk>\d+)/$', views.school_detail, name='school_detail'),
	url(r'^school/(?P<pk>\d+)/edit/$', views.school_edit, name='school_edit'),
]
