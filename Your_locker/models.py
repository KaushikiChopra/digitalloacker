from django.db import models

# Create your models here.
class Home(models.Model):
    text = models.CharField(max_length=500)
    home_title= models.CharField(max_length=250)
    upload = models.FileField (max_length=1000)

    def __str__(self):
        return self.home_title
        
    
    



    


    
    


    
