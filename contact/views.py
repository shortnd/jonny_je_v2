from django.shortcuts import render, redirect
from django.core import mail

from .form import ContactForm


def contact_page(request):
    contact_form = ContactForm

    if request.method == 'POST':
        form = contact_form(request.POST)

        if form.is_valid():
            contact_subject = request.POST.get(
                'contact_subject', ''
            )
            contact_name = request.POST.get(
                'contact_name', ''
            )
            contact_email = request.POST.get(
                'contact_email', ''
            )
            contact_textarea_content = request.POST.get(
                'text_area_content', ''
            )

            # Email the content of the form as dict
            context = dict({
                'contact_subject': contact_subject,
                'contact_name': contact_name,
                'contact_email': contact_email,
                'contact_textarea_content': contact_textarea_content,
            })

            mail.send_mail(
                           # Subject
                           context['contact_subject'],
                           # Message
                           context['contact_textarea_content'],
                           # Contact Email/Client
                           "from@example.com",
                           # To Email/Who to send it to
                           # must be an array list
                           # are able to have multiple
                           # ['contact@jonnyje.com', 'coconnell@jonnyje.com']
                           [''],
                           fail_silently=True)
        return redirect('thank_you')

    return render(request, 'contact/contact.html', {
        'contact_form': contact_form,
    })
