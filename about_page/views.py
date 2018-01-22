from django.shortcuts import render, HttpResponse


def about_page(request):
    return render(request, 'about_page/about_page.html')
