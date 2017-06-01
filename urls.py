"""seatsys URL Configuration

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
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url,include
from django.contrib import admin
from login import urls as login_urls
from seat import views as seat_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/',include(login_urls)),
    #seat系统
    url(r'^statuscheck/',seat_views.statuscheck,name='statuscheck'),
    url(r'^status/',seat_views.status),
    url(r'^seatinfo/',seat_views.seatinfo),
    url(r'^seat/order',seat_views.order),
    url(r'^seat/seatinfo/$',seat_views.seatinfo),
]
