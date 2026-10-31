from django.db import models
from django.contrib.auth.models import User


class Skill(models.Model):
    SKILL_TYPES = [
        ('teach', 'Can Teach'),
        ('learn', 'Wants to Learn'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    skill_type = models.CharField(
        max_length=10,
        choices=SKILL_TYPES
    )
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.name}"


class SkillExchangeRequest(models.Model):
    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='sent_requests'
    )

    receiver = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='received_requests'
    )

    offered_skill = models.ForeignKey(
        Skill,
        on_delete=models.CASCADE,
        related_name='offered_in_requests'
    )

    requested_skill = models.ForeignKey(
        Skill,
        on_delete=models.CASCADE,
        related_name='requested_in_requests'
    )

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.username} -> {self.receiver.username}"