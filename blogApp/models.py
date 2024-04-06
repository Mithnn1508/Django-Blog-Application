from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length = 80)
    content = models.TextField()
    published_date= models.DateTimeField(auto_now_add=True)
    last_updated_on = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name = "user_posts")
    likes = models.ManyToManyField(User)


class Comment(models.Model):
    content = models.TextField()
    created_on = models.DateField(auto_now_add=True)
    post_on = models.ForeignKey(Post,on_delete=models.CASCADE,related_name="post_comments")
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name = "comment_user")