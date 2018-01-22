from django.shortcuts import render

from .models import OurWork


def our_work(request):
    """Show all the work"""
    work = OurWork.objects.all()
    context = {'our_work': work}
    return render(request, 'our_work/our_work.html', context)
