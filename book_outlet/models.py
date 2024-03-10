from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=50)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.CharField(max_length=100, null=True)
    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="",null=False, db_index=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('book-detail', args=[self.id])

    def _str_(self):
        return f"{self.rating} ({self.title})"