from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from product.models import Product
from .forms import ContactForm

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            recipients = ['eocean394@gmail.com']
            send_mail(f"Submisson from {name} :",message+" - "+from_email, from_email, recipients)
            messages.warning(request, 'Thank you for the submission. We aim to repsond within 4 working days.')
            form = ContactForm()
    else:
        form = ContactForm()
    return render(request, 'contact-form.html', {'form': form})

def priv_pol(request):
    return render(request, 'policy.html', {})


def landing(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'home.html', context)