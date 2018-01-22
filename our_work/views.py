from django.shortcuts import render, HttpResponse


def our_work(request):
    return HttpResponse('<h2>Our Work</h2>')
