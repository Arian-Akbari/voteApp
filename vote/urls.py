from django.urls import path

from . import views

urlpatterns = [
    path("", views.start, name="start"),
    path("finish/", views.finish, name="finish"),
    path("results/", views.results, name="results"),
    path("select/<str:name>/", views.select, name="select"),
]

