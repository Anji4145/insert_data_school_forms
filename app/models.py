from django.db import models

# Create your models here.
class school(models.Model):
    scname=models.CharField(max_length=20,primary_key=True)
    scprincipal=models.CharField(max_length=20)
    sclocation=models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.scname
    
class student(models.Model):
    stid=models.IntegerField(primary_key=True)
    stname=models.CharField(max_length=20)
    scname=models.ForeignKey(school,on_delete=models.CASCADE)
    
    

    def __str__(self) -> str:
        return self.stname   