from django.db import models

class Users(models.Model):
    ROLL_CHOICES = [
        ('admin', 'Admin'),
        ('user', 'User')
    ]
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, verbose_name='email')
    role = models.CharField(max_length=10, choices=ROLL_CHOICES, default='user')

    def __str__(self):
        return f"{self.name} ({self.role})"

