from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.OneToOneField("User", on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    agent = models.ForeignKey("Agent", on_delete=models.CASCADE)


class User(AbstractUser):
    # Fields - username , first_name , last_name , email , is_staff , is_superuser , is_active , date_joined
    pass


class Agent(models.Model):
    user = models.OneToOneField("User", on_delete=models.CASCADE)
    organisation = models.ForeignKey("UserProfile", on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


def post_user_created_signal(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

# Attaching an event to a model right after it is committed to the DB, to attach right before use pre_save()
# It will share with us sender, instance-model instance that was saved , created-boolean indicating if it was created
# (like if it was updated then this won't ber true


post_save.connect(post_user_created_signal, sender=User)
