

from django.urls import path

from shortner.views import shortner,redirector

urlpatterns = [
    path("", shortner, name="shortner"),
    path("<str:pk>/", redirector, name="redirector")
]
