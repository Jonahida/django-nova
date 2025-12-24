from django.db import models
from django.contrib.auth.models import User

class NovaPage(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class NovaBlock(models.Model):
    BLOCK_TYPES = [
        ("text", "Text"),
        ("image", "Image"),
        ("list", "List"),
    ]
    page = models.ForeignKey(NovaPage, related_name="blocks", on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=BLOCK_TYPES)
    content = models.JSONField(default=dict)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.page.title} — {self.type} #{self.order}"

