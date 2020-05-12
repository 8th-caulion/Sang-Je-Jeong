from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    memo = models.TextField(null=True, default='')
    cata = models.TextField(null=True, default='')
    
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:50]