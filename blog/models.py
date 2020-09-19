from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.template.defaultfilters import slugify
from taggit.managers import TaggableManager

from ckeditor.fields import RichTextField

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    header = models.ImageField(blank=True, null=True, upload_to="images/")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = TaggableManager()
    likes = models.ManyToManyField(User, related_name="blog_post")
    body = RichTextField(blank=True, null=True)
    # body = models.TextField() #plain body text
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title + " | " + str(self.author)

    def get_absolute_url(self):
        # in order  go to the url named 'details' and pass in self.pk
        # return reverse('details', kwargs={'slugx': self.slug})
        # in order to redirect to home page after writing a new post
        return reverse("home")

    def save(self, *args, **kwargs):  # pass in args just in case
        if not self.id:  # if it's a new post, make a slug
            candid = slugify(self.title)
            duplicates = len(Post.objects.filter(slug=candid))
            if duplicates > 0:  # if already exists
                for i in range(duplicates):
                    candid += "_re" + str(i + 1)
            self.slug = slugify(self.title)
        return super(Post, self).save(*args, **kwargs)

    def total_likes(self):
        return self.likes.count()
