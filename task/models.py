from django.db import models
from django.utils import timezone

# Create your models here.
class Task(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed')
    ]

    PRIORITY_CHOICES = [
        ('Low', 'Low'),
        ('Medium', 'Medium'),
        ('High', 'High')
    ]

    name = models.CharField(max_length=300)
    status = models.CharField(max_length=20, choices = STATUS_CHOICES, default='Pending')
    created_date = models.DateField(default=timezone.now)
    expiry_date = models.DateField(default=timezone.now)
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default='Medium')
    
    def __str__(self):
        return self.name