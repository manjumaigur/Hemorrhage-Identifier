from django.conf.urls import include, url
from . import views

app_name = 'hemorrhage'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^add-image/$', views.identify_hemorrhage, name='image-form'),
	url(r'^output/(?P<pk>\d+)/$', views.output, name='output'),
]