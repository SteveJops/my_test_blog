from distutils.command import upload
from tabnanny import verbose
from turtle import title
from django.db import models

class BlogPosts(models.Model):
    """Blog class"""
    blog_title = models.CharField("Blog Title", max_length=50)
    blog_date = models.DateTimeField("Blog Date", auto_now_add=True)
    blog_text = models.TextField("Main Text")
    blog_image = models.ImageField("Blog Image", upload_to = 'blog/')

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self) -> str:
        return self.blog_title