from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Hospital(models.Model):
    hospital_name = models.CharField(max_length=50)
    hospital_addr = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'hospital'


class Caregiver(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE, related_name="caregiver")
    caregiver_cd = models.CharField(max_length=50, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'caregiver'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    caregiver = models.ForeignKey(Caregiver, on_delete=models.CASCADE, related_name="caregiver", null=True)
    training_status = models.CharField(max_length=10, default='0')

    class Meta:
        db_table='auth_profile'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class FCMToken(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="fcm_token")
    token = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Inpatiant(models.Model):
    caregiver = models.ForeignKey(Caregiver, on_delete=models.CASCADE, related_name="inpatiant")
    inpatiant_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=2)
    birth = models.CharField(max_length=20)
    persnal_cd = models.CharField(max_length=50)
    important = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'inpatiant'


class InpatiantChildren(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="inpatiant_children")
    inpatiant = models.ForeignKey(Inpatiant, on_delete=models.CASCADE, related_name="inpatiant_children")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'inpatiant_children'


class VoiceSample(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="voice_sample")
    file_path = models.CharField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'voice_sample'


class VoiceCloiningModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="voice_cloining_model")
    model_path = models.CharField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'voice_cloining_model'

