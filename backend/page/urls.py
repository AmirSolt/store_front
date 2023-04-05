from django.urls import path

from . import views

urlpatterns = [
    path("<str:page_name>", views.page, name="page"),
    path("<str:page_name>/edit", views.edit, name="edit"),
]