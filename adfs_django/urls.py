"""adfs_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
import django_saml2_auth.views
from django.conf.urls import url, include
from django.contrib import admin
from .views import IndexPageView, LogoutView, RestView

urlpatterns = [
    url('oauth2/', include('django_auth_adfs.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^logout$', LogoutView.as_view()),
    url(r'^api/test$', RestView.as_view()),
    url(r'^.*', IndexPageView.as_view())
]
