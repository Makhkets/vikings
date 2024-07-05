from django.db import models

class Photo(models.Model):
    model_field = models.ImageField(upload_to='photos/', verbose_name='mphoto')
    photo_name = models.CharField(max_length=100, verbose_name="Photo name")

    def __str__(self):
        return self.photo_name

    class Meta:
        verbose_name = 'photo'
