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


class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    caregiver = models.ForeignKey(Caregiver, on_delete=models.CASCADE, related_name="caregiver")

    class Meta:
        db_table='auth_profile'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Inpatiant(models.Model):
    caregiver = models.ForeignKey(Caregiver, on_delete=models.CASCADE, related_name="inpatiant")
    inpatiant_name = models.CharField(max_length=20)
    gender = models.CharField(max_length=2)
    birthdate = models.CharField(max_length=20)
    persnal_cd = models.CharField(max_length=50)
    important = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'inpatiant'


class Inpatiant_children(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="inpatiant_children")
    inpatiant = models.ForeignKey(Inpatiant, on_delete=models.CASCADE, related_name="inpatiant_children")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'inpatiant_children'


class Voice_sample(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="voice_sample")
    file_path = models.FileField(upload_to='voice_sample')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'voice_sample'


class Voice_cloining_model(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="voice_cloining_model")
    model_path = models.FileField(upload_to='voice_cloining_model')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'voice_cloining_model'

