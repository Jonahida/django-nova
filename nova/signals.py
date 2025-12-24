from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import NovaPage

@receiver(post_save, sender=NovaPage)
def on_page_save(sender, instance, created, **kwargs):
    if created:
        print(f"New page created: {instance.title}")

