from django.conf.urls import url
from . import views

app_name = 'first'

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^(?P<area_id>[0-9]+)/$', views.detail, name="detail"),
    url(r'^(?P<area_id>[0-9]+)/details/$', views.Display_detail, name="display"),
    url(r'^(?P<area_id>[0-9]+)/input_person/$', views.inputperson, name="inputperson"),
    url(r'^p_detail/', views.personindex, name='p_detail')

]
