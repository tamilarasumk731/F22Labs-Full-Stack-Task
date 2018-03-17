from __future__ import unicode_literals

from django.db import models
from PIL import Image as im
from PIL import ImageFilter as imf



class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
