from django.db import models
from django.forms import ValidationError


def validate_file_extension(value):
    import os
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.py']
    if not ext in valid_extensions:
        raise ValidationError('File not supported!')
# Create your models here.


class UploadScript(models.Model):
    # upload a file to the server
    # file_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    description = models.TextField()
    file = models.FileField(upload_to='scripts/',validators=[validate_file_extension])
    image = models.ImageField(upload_to='scripts/thumbnails/')
    created_at = models.DateTimeField(auto_now_add=True)
    # upload a file to the server
    # upload a file to the server


class UploadImage(models.Model):
    image = models.ImageField(upload_to='images')
    converted_image = models.ImageField(upload_to='images')
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption
