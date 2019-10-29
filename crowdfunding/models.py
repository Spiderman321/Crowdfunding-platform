from django.db import models

# Create your models here.
class Sponsor(models.Model):
    name = models.CharField(max_length=10)
    phoneNum = models.IntegerField()
    idNum = models.AutoField(primary_key=True)
    content = models.TextField()

    def __str__(self):
        return self.name

