"""Elearning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Elearning import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('course.urls')),
    path('account/', include('account.urls')),
    path('confidentialite/', views.confidentialite, name="confident" ),
    path('dash/', views.dashboard, name="dash"),
    path('donate/', views.donate, name="donation"),
    path('nos-cours', views.cours, name="nos-cours"),
    path('dev-cours', views.courss, name="dev-cours"),
    path('contact/', include('contact.urls')),
    path('cours2', views.cours2, name="gestion-cours")
]