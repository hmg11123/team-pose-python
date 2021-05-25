from django.urls import path
from contacts import views as contact_views

app_name = "contact"

urlpatterns = [
    path("send/", contact_views.renderContact, name="send"),
]