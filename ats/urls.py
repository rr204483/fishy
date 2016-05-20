from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^myview/$', views.curr_datetime),
    url(r'^schooladd/$', views.create_school, name="school"),
]
