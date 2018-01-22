from django.urls import path

from . import views


app_name = 'our_work'
urlpatterns = [
    path('', views.our_work, name='our_work'),
]
