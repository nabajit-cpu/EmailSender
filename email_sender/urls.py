# email_sender/urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^send-email/$', views.send_email_view, name='send_email'),  # Define the send email route
]
