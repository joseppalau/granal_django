from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('cesped-artificial/', views.cesped_artificial_page, name='cesped-artificial'),
    path('cesped-natural/', views.cesped_natural_page, name='cesped-natural'),
    path('equipamiento-deportivo/', views.equipamiento_deportivo_page, name='equipamiento-deportivo'),
    path('pavimentos-deportivos/', views.pavimentos_deportivos_page, name='pavimentos-deportivos'),
    path('contact/', views.emailView, name='email'),
    path('contact/success/', views.successView, name='success'),
]