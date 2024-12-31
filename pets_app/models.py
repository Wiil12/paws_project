from django.db import models

# Create your models here.
class Pet(models.Model):
    petName = models.CharField(max_length=255, null=True)
    petAge = models.IntegerField(null=True)
    petBreed = models.CharField(max_length=255, null=True)
    petImage = models.CharField(max_length=500, null=True)
    
    class meta:
        db_table = "pets"
        
        
class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
 
    class Meta:
        db_table="blog"