from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("index", views.index, name="index"),
    path("files", views.files,name="files"),
    path("companies", views.companies,name="companies"),
    path("file-details/<int:id>", views.fileDetails, name="fileDetails"),
    path('download/<int:id>/', views.download, name='download')  

]