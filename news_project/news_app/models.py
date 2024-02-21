from django.db import models
from datetime import datetime

class Post(models.Model):
    title = models.CharField("Caption", max_length=50)
    description = models.TextField("Content")
    image = models.CharField("URL image", max_length=500)
    post_date = models.DateTimeField("Date and publication time", default=datetime.now)
    
    def __str__(self):
        return f"{self.title}"