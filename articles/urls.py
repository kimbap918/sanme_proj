from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path("", views.index, name="index"),
    path("postall/", views.postall, name="postall"),
    path("create/", views.create, name="create"),
    path("<int:pk>/comment/", views.comment, name="comment"),
    path("<int:pk>/", views.detail, name="detail"),
    path("<int:pk>/update/", views.update, name="update"),
    path("<int:pk>/delete/", views.delete, name="delete"),
    path("<int:pk>/comment/", views.comment, name="comment"),
]
