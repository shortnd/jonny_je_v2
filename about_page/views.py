from django.shortcuts import render, HttpResponse


def about_page(request):
    return HttpResponse('<h1>About page</h1>')
