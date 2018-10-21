from io import BytesIO

from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils.text import slugify
from PIL import Image
from resizeimage import resizeimage


def profile_avatar_path(instance, filename):
    return 'avatars/{0}/{1}'.format(instance.slug, filename)


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE)
    slug = models.SlugField(null=True, blank=True)
    bio = models.TextField(max_length=240, blank=True)
    avatar = models.ImageField(
        upload_to=profile_avatar_path, default='avatars/no-img.png')
    city = models.CharField(max_length=50, blank=True)
    state = models.CharField(max_length=50, blank=True)
    birthday = models.DateField(null=True, blank=True)
    joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('profile', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
