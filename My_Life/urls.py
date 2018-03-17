"""My_Life URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from music import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.homepage, name="homepage"),
    url(r'^add/',views.addsong, name="addsong"),
    url(r'^deletesong/',views.deleteSong, name="deletesong"),
    url(r'search/',views.search_music, name="search_music"),
    url(r'^userpage/(?P<username>[-\w]+)/$', views.PlayListView.as_view(), name="user_page"),
    url(r'^account/',include("account.urls"), name="account"),
    url(r"^account/", include("django.contrib.auth.urls")),
    url(r"^brand/", views.BrandPlayListView.as_view(), name="brand")
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls))
    ] + urlpatterns