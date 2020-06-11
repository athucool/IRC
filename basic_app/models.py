from django.db import models

# Create your models here.
class IRC_API(models.Model):
    date_time=models.DateTimeField(("date_time"), auto_now=False, auto_now_add=False)
    url=models.URLField(("url"), max_length=200)
    

    def __str__(self):
        return self.url
    
     