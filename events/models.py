from asyncio import events
from distutils.command.upload import upload
from django.db import models


class Event(models.Model):
    """ Event class """
    event_image = models.ImageField('Image', upload_to='events/')
    event_text = models.CharField("Description", max_length=350)

