from django.urls import path

from . import views


app_name = "contact"
urlpatterns = [
    path('', views.contact_page, name='contact'),
    path('thank_you/', views.thank_you, name='thank_you'),
]
