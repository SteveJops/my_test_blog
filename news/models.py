from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.text import slugify
from time import time

User = get_user_model()

def gen_slug(s):
    new_slug - slugify(s, allow_unicode=True)
    return new_slug + '-' + str(int(time()))



class News(models.Model):
    """ News class """
    user = models.ForeignKey(User, verbose_name="Author", on_delete=models.CASCADE)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    title = models.CharField('Title', max_length=50)
    text_min = models.TextField("Description", max_length=350)
    text = models.TextField("Articles text")
    created = models.DateTimeField( auto_now_add=True)
    image = models.ImageField('Image', upload_to='news/')
    

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"
    

    def absolute_url(self):
        return reverse('single_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    
    def __str__(self) -> str:
        return self.title

