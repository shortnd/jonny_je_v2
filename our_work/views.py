from django.shortcuts import render


def our_work(request):
    return render(request, 'our_work/our_work.html')
