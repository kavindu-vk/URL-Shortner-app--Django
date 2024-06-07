from django.db import models
from django.utils.crypto import get_random_string

class URL(models.Model):
    original_url = models.URLField()
    short_url = models.CharField(max_length=10, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = get_random_string(6)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.original_url} -> {self.short_url}'
