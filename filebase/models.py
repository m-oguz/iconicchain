from django.db import models
from datetime import datetime
from django.contrib.auth.models import User,Group
# Create your models here.


class File(models.Model):
    name = models.CharField(max_length=100, default="File")
    file = models.FileField(upload_to="files/")
    download_counter = models.IntegerField(default=0)
    upload_date = models.DateTimeField(default=datetime.now())
    description = models.TextField(max_length=400, default="Description of the file")
    uploader = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    company = models.ForeignKey(Group,on_delete=models.CASCADE,default=1)