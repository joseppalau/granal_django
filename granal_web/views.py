from django.shortcuts import render

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


