from django.db import models

# Create your models here.


class Team(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=1024)


class Player(models.Model):
    STATUS = (
        ('Primary', 'Primary'),
        ('Sub', 'Sub'),
        ('Ineligible', 'Ineligible'),
    )
    name = models.CharField(max_length=1024)
    full_name = models.CharField(max_length=1024)
    team = models.ForeignKey(Team, blank=False, null=False)
    status = models.CharField(
        choices=STATUS,
        default='Primary',
        max_length=1024,
    )
    updated = models.DateTimeField(blank=False, null=False)