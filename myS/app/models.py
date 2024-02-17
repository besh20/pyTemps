from django.db import models

# Create your models here.

class company(models.Model):
    name = models.CharField(max_length = 50)
    motto = models.TextField(default = 'Get Your Greatest Fit') 

    def __str__(self) -> str:
        return self.name

class catagory(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self) -> str:
        return self.name


class products(models.Model):
    image  = models.ImageField(null = True)
    name = models.CharField(max_length = 50)
    catagory = models.ForeignKey(catagory, on_delete = models.CASCADE)
    price = models.FloatField(null = True)

    def __str__(self) -> str:
        return self.name
