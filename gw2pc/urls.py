"""lightdelay URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from django.views.generic import TemplateView

from gw2pc import views

urlpatterns = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + [
    path('about/',
         TemplateView.as_view(template_name="gw2pc/about.html"),
         name='about'),
    path('docs/',
         TemplateView.as_view(template_name="gw2pc/docs.html"),
         name='docs'),
    path('sitemap.xml',
         TemplateView.as_view(template_name="gw2pc/sitemap.xml"),
         name='sitemap'),
    path('robots.txt',
         TemplateView.as_view(template_name="gw2pc/robots.txt"),
         name='robots.txt'),
    path('',
         TemplateView.as_view(template_name="gw2pc/homepage.html"),
         name='gw2pc_homepage'),
    # Ugly re_path URLs are basically required here because APPEND_SLASH just
    # straight up doesn't work with zappa, so we either need two `path` urls
    # (one with, one without), or a regex with an optional slash.
    re_path('^t3/?$',
         views.T3SetView.as_view(),
         name='gw2pc_t3'),
    re_path('^t4/?$',
         views.T4SetView.as_view(),
         name='gw2pc_t4'),
    re_path('^t6/?$',
         views.T6SetView.as_view(),
         name='gw2pc_t6'),
    re_path('^mc/?$',
         views.MCView.as_view(),
         name='gw2pc_mc'),
    re_path('^ecto/?$',
         views.EctoView.as_view(),
         name='gw2pc_ecto'),
    re_path('^leg/?$',
         views.gw2pc_leg,
         name='gw2pc_leg'),
]
