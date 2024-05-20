from django.db import models

class NewCars(models.Model):
    name = models.CharField(max_length=30)
    desc = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='pics')

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class FeaturedCars(models.Model):
    name = models.CharField(max_length=30)
    desc = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='pics')
    
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url