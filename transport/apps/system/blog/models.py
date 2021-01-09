from django.db import models
from django.db.models.signals import pre_save
from .utils import unique_slug_generator


class Tutorial (models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(max_length=150, unique=True)

    def __str__(self):
        return self.title
        
def slug_save(sender, instance, *args, **kwargs):
    if not instance.slug:#if slug dont exist
        instance.slug = unique_slug_generator(instance, instance.title, instance.slug)

pre_save.connect(slug_save, sender=Tutorial)