import uuid
from django.db import models
from django.utils.timesince import timesince

from account.models import User

# Create your models here.


class Message(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        User,
        related_name="created_by",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    class Meta:
        ordering = ("created_at",)

    def __str__(self) -> str:
        return f"{self.sent_by}"


class Room(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    participants1 = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="participants1"
    )
    participants2 = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="participants2"
    )

    messages = models.ManyToManyField(Message, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def modified_at_formatted(self):
        return timesince(self.modified_at)

    class Meta:
        ordering = ("-created_at",)

    def __str__(self) -> str:
        return f"{self.participants1} - {self.id}"
