"""workshop_portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from workshop_app import views
#from chatterbot.ext.django_chatterbot import urls as chatterbot_urls
import django

js_info_dict = {
    'packages': ('recurrence', ),
}


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('workshop_app.urls')),
    url(r'^', include('workshop_app.urls_password_reset')),
    url(r'^', include('statistics_app.urls')),

]
