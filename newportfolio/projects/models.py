from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from topics.models import Topic

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/%Y/%m/%d/', blank=True, null=True) # store images based on date created
    slug = models.SlugField(unique=True, blank=True)

    topics = models.ManyToManyField(Topic, related_name='projects', blank=True) # reverse look up

    updated = models.DateTimeField(auto_now=True) # get timestamp for whenever this is updated
    created = models.DateTimeField(auto_now_add=True) # get timestamp when instance was first created

    def __str__(self):
        return self.title
    
    # dynamically generate a URL for the detail view of a project based on its slug
    def get_absolute_url(self):
        return reverse("project_detail", kwargs={"slug": self.slug}) # resolves a URL pattern name into actual URL
    
    # generate a slug based on the project title
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    # newest project first
    class Meta:
        ordering = ['-created']
