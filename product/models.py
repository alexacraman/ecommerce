from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.files.storage import FileSystemStorage
import uuid

class Product(models.Model):
    name        = models.CharField(max_length=200, db_index=True)
    slug        = models.SlugField(max_length=200, db_index=True)
    file        = models.FileField(upload_to='protected',storage=FileSystemStorage(location=settings.PROTECTED_ROOT))
    image       = models.ImageField(blank=True)
    description = models.TextField(blank=True)
    price       = models.DecimalField(max_digits=10, decimal_places=2)
    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:detail', kwargs={'id':self.id,'slug': self.slug})

    def get_download_url(self): # detail view
        return reverse("products:download", kwargs={'id':self.id,'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.name)
            unique_slug = str(uuid.uuid4())[:1]
            self.slug = f"{base_slug}-{unique_slug}"
        return super().save(*args, **kwargs)

