from django.db import models

class Post(models.Model):
    title = models.CharField()
    text = models.TextField()

    def __str__(self):
        return self.title