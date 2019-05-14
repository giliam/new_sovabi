# coding: utf-8

from django.conf.urls import url

from messes import views

urlpatterns = [
    url(r'^liste/$', views.liste_messes,
        name="messes_liste"),
]