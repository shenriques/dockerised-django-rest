from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    slug = models.SlugField(unique=True, blank=True)

    updated = models.DateTimeField(auto_now=True) # get timestamp for whenever this is updated
    created = models.DateTimeField(auto_now_add=True) # get timestamp when instance was first created

    def __str__(self):
        return self.title
    
    # dynamically generate a URL for the detail view of a article based on its slug
    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.slug}) # resolves a URL pattern name into actual URL
    
    # generate a slug based on the article title
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    # newest article first
    class Meta:
        ordering = ['-created']
