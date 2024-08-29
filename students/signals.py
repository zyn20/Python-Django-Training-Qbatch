# myapp/signals.py

from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from students.models import DummyTable


@receiver(pre_save, sender=DummyTable)
def pre_save_signal(sender, instance, **kwargs):
    print(f"pre_save signal triggered for {instance.full_name}")


@receiver(post_save, sender=DummyTable)
def post_save_signal(sender, instance, **kwargs):
    print(f"post_save signal triggered for {instance.full_name}")
