from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    caption = models.TextField(max_length=512)

# class Comment(models.Model):
#     pass

# class Like(models.Model):
#     pass
