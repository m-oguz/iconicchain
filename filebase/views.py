from django.shortcuts import get_object_or_404, render
from django.http.response import HttpResponse
from .models import File
from django.contrib.auth.models import User,Group


# Create your views here.


def index(request):
    filesToShow = 20
    users = []

    files = File.objects.order_by('-download_counter')[:filesToShow]
    for file in files:
        users.append(file.uploader)


    context = {
        "files" :  files,
        "users" : users,
    }
    return render(request, "filebase/index.html",context)


def files(request):
    context = {
        "files" : File.objects.all(),
        "users" :  User.objects.all()
    }
    return render(request, "filebase/files.html",context)

def companies(request):
    context = {
        "companies" : Group.objects.all()
    }
    return render(request, "filebase/companies.html", context)

def fileDetails(request, id):
    return render(request, "filebase/file-details.html",{
        "id" : id
    })


def download(request, id):
    file = get_object_or_404(File,pk=id)
    response = HttpResponse(file.file, content_type='application/force-download')
    response['Content-Disposition'] = f'attachment; filename={file.file.name}'
    file.download_counter +=1
    file.save()
    return response