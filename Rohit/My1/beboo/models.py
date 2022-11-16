from django.db import models

# Create your models here.
class Brainwork(models.Model):
    Title=models.CharField(max_length=50,null=True)
    Descriptions=models.TextField(null=True)
