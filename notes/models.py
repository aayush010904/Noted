from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Notes(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    tags = models.ManyToManyField(Tag, blank=True, related_name='notes')

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title
    

