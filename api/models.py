from django.db import models


class Incident(models.Model):
    STATUS_CHOICES = [
        ('active', 'active'),
        ('closed', 'closed'),
    ]

    title = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')

    def __str__(self):
        return self.title