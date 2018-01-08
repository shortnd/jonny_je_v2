from django.shortcuts import render, HttpResponse


def home_page(request):
    return HttpResponse('<html><head><title>Home | JonnyJE Technical Support</title></head><body><h1>Home Page JonnyJE Technical Support</h1></body></html>')
