from django.conf.urls import url

from . import views

app_name = 'about_page'
urlpatterns = [
    url(r'^$', views.about_page, name='about_page'),
]
