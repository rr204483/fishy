from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^home/$', views.home),
    #url(r'^addstudent/$', views.create_school, name="schooladd"),
   # url(r'^liststudents/$', views.list_schools, name="list_schools"),
	#url(r'^school/(?P<pk>\d+)/$', views.school_detail, name='school_detail'),
	#url(r'^school/(?P<pk>\d+)/edit/$', views.school_edit, name='school_edit'),
]
