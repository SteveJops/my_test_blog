from tabnanny import verbose
from turtle import title
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()



class News(models.Model):
    """ News class """
    user = models.ForeignKey(User, verbose_name="Author", on_delete=models.CASCADE)
    title = models.CharField('Title', max_length=50)
    text_min = models.TextField("Description", max_length=350)
    text = models.TextField("Articles text")
    created = models.DateTimeField('Date of creation', auto_now_add=True)
    image = models.ImageField('Image', upload_to='news/')
    

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"
    

    def __str__(self) -> str:
        return self.title

