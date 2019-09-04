"""sample_django URL Configuration

The `urlpatterns` list routes URLs to vyus. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function vyus
    1. Add an import:  from my_app import vyus
    2. Add a URL to urlpatterns:  url(r'^$', vyus.home, name='home')
Class-based vyus
    1. Add an import:  from other_app.vyus import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from firstapp.vyus.hello import  hi, hi_with_template
from firstapp.views import create_site, send_email, login
from django.views.generic import ListView
from firstapp.model.dream_real import Dreamreal
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/(\d+)/', hi),
    url(r'^hi/(\d+)/', hi_with_template),
    url(r'^create_site/(\w+)/(\w+)', create_site, name= 'blabla'),
    url(r'^send_email/(\w+)', send_email, name='email'),
    url(r'^dream_reals/', ListView.as_view(model = Dreamreal,
      template_name = "dreamreal_list.html"), name='static'),
    url(r'^login/', login, name='loggedin'),
    url(r'^connection/',TemplateView.as_view(template_name = 'login.html'), name='login'),

]
