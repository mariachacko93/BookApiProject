from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.

class Author(models.Model):
    author=models.CharField(max_length=30)

    def __str__(self):
        return self.author
        
class Book(models.Model):
    author=models.ManyToManyField(Author)
    bookname=models.CharField(max_length=120,null=True)
    pages=models.IntegerField(null=True)
    pubyear=models.IntegerField(null=True)
    abstract=models.TextField(max_length=400,null=True)

    def __str__(self):
        return self.bookname




@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)