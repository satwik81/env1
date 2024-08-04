from django.db import models


class filecsv(models.Model):
    file=models.FileField(upload_to='tmp/')
    uploadto=models.DateTimeField(auto_now_add=True)
    

# Create your models here.
