from django.urls import path
from . import views
app_name = "urlShortener"
urlpatterns=[
    path("", views.index, name="index" ),
    path("shortenUrl", views.shortenUrl, name="shortenUrl")
]