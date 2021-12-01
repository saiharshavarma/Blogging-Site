from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics')
    slug = models.SlugField(max_length=264, unique=True, editable=False)

    def __str__(self):
        return f'{self.user.username}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.username, allow_unicode=True)
        super().save(*args, **kwargs)