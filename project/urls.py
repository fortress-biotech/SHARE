"""share URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.contrib import admin
from django.conf.urls import url, include
from revproxy.views import ProxyView

urlpatterns = [
    url(r'^admin(/|$)', admin.site.urls),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api(/|$)', include('api.urls', namespace='api')),
    url(r'^o(/|$)', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^accounts(/|$)', include('allauth.urls')),

    # TODO ember url in settings, maybe a separate view
    url(r'^(?P<path>.*)$', ProxyView.as_view(upstream='http://localhost:4200/')),
]
