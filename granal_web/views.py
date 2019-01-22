from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.template.loader import get_template
from django.http import HttpResponse
from .forms import ContactForm
from django.conf import settings


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
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            number = form.cleaned_data['number']
            template = get_template('granal_web/contact_template.txt')
            context = {'subject': subject, 'from_email': from_email, 'message': message, 'number': number}
            content = template.render(context)
            send_mail('Nuevo formulario de Contacto',
                                 content, settings.DEFAULT_FROM_EMAIL,
                                 ['jeppalau83@gmail.com'], fail_silently=True
                                 )
            return redirect('success')
    return render(request, 'granal_web/contact.html', {'form': form})

def successView(request):
    return HttpResponse('Success! Thak you for your message.')

