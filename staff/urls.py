from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^home/$', views.home),
    url(r'^staffadd/$', views.create_staff, name="staffadd"),
    url(r'^liststaff/$', views.list_staff, name="list_staff"),
	url(r'^staff/(?P<pk>\d+)/$', views.staff_detail, name='staff_detail'),
	url(r'^staff/(?P<pk>\d+)/edit/$', views.staff_edit, name='staff_edit'),
	url(r'^delete/(?P<pk>\d+)/$', views.StaffDelete.as_view(), name="delete_staff")
]
