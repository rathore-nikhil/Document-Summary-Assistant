from django.db import models

# Create your models here.
class Document(models.Model):
    uploaded_file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
