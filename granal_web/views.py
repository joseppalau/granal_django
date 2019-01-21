from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from .forms import ContactForm

def home_page(request):
    return render(request, 'granal_web/index.html')

def cesped_artificial_page(request):
    return render(request, 'granal_web/cesped-artificial.html')

def cesped_natural_page(request):
    return render(request, 'granal_web/cesped-natural.html')

def equipamiento_deportivo_page(request):
    return render(request, 'granal_web/equipamiento-deportivo.html')

def pavimentos_deportivos_page(request):
    return render(request, 'granal_web/pavimentos-deportivos.html')

def emailView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['jeppalau83@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'granal_web/contact.html', {'form': form})

def successView(request):
    return HttpResponse('Success! Thak you for your message.')

