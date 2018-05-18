"""ouragan_opp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import include ,path
from django.views.generic import TemplateView
from ouragan.views import ContactView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='pages/index.html'), name='home'),
    path('contact/', ContactView.as_view(template_name='pages/contact.html'), name='contact'),
    path('opportunites/', TemplateView.as_view(template_name='pages/opportunites.html'), name='opportunites'),
    path('opportunites/m', TemplateView.as_view(template_name='pages/m.html'), name='m'),
    path('opportunites/e', TemplateView.as_view(template_name='pages/e.html'), name='e'),
    path('opportunites/a', TemplateView.as_view(template_name='pages/a.html'), name='a'),
    path('team/', TemplateView.as_view(template_name='pages/team.html'), name='team'),
    path('eagle_pub/', TemplateView.as_view(template_name='pages/eagle_pub.html'), name='eagle_pub'),
    path('f/', include('formation.urls')),
]
