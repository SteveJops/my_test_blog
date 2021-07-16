
from django.db import models


class Event(models.Model):
    """ Event class """
    event_image = models.ImageField('Image', upload_to='events/')
    event_text = models.CharField("Description", max_length=350)

    class Meta:
        verbose_name = "Event"
        verbose_name_plural = "Events"
    

    def __str__(self) -> str:
        return self.event_text[:10]

