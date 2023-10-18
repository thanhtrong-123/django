from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('HomeView')

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField(blank=True, null=True)
    header_image = models.ImageField(null=True,blank=True, upload_to="images/")
    # body = models.TextField()
    draft = models.BooleanField(default=True)
    # publish = models.DateField(auto_now=False,auto_now_add=False)
    post_date = models.DateField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=False,auto_now_add=True)
    timestamp = models.DateTimeField(auto_now=True,auto_now_add=False)
    likes = models.ManyToManyField(User, related_name='blog_posts')
    category = models.CharField(max_length=255, default="coding")

    def total_likes(self):
        return self.likes.count()
        
    def __str__(self):
        return self.title + ' | ' + str(self.author)
    
    def get_absolute_url(self):
        return reverse('HomeView')

class Profile(models.Model):
    user = models.OneToOneField(User, null= True, on_delete=models.CASCADE)
    bio =models.TextField()
    profile_pic = models.ImageField(null=True,blank=True, upload_to="images/profile")
    

    def __str__(self):
        return str(self.user)
    
    def get_absolute_url(self):
        return reverse('HomeView')
    
    


class Comment(models.Model):
    post = models.ForeignKey(Post,related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)
    