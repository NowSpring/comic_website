from django.db.models.signals import post_save
from django.dispatch import receiver
# from accounts.models import User
from django.contrib.auth.models import User
from comics.models import Comic
from .models import Review

@receiver(post_save, sender=User)
def create_user_reviews(sender, instance, created, **kwargs):
    if created:
        comics = Comic.objects.all()
        for comic in comics:
            Review.objects.create(user=instance, comic=comic)

@receiver(post_save, sender=Comic)
def create_comic_reviews(sender, instance, created, **kwargs):
    if created:
        users = User.objects.all()
        for user in users:
            Review.objects.create(user=user, comic=instance)
