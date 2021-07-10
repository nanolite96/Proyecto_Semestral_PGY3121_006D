from django.conf.urls import url
from rest_framework import urlpatterns
from api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^api/trabajos/$',views.TrabajosViewSet.as_view()),
    url(r'^api/contactos/$',views.ContactoViewSet.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)