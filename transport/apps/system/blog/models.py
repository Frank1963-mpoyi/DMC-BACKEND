from django.db import models




class DestinationCompany (models.Model):
    title = models.CharField(max_length=150)
    # slug = models.SlugField(max_length=150, unique=True)
    image =  models.ImageField(upload_to='pictures')
    name = models.CharField(max_length=150, null=True, blank=True)
    dsm = models.BooleanField(default=False)

    def __str__(self):
        return self.title
