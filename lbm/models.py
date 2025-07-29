import uuid
import os
from django.db import models


def path_and_rename(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4().hex}.{ext}"
    return os.path.join('medias/', filename)


class Media(models.Model):
    CATEGORIES = [
        ('DECORATION', 'Décoration'),
        ('ICON', 'Icône'),
    ]
    name = models.CharField(max_length=200, blank=True)
    category = models.CharField(max_length=20, choices=CATEGORIES)
    file = models.ImageField(upload_to=path_and_rename)

    def save(self, *args, **kwargs):
        if not self.name and self.file:
            filename = os.path.splitext(os.path.basename(self.file.name))[0]
            self.name = filename
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.file.delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.name