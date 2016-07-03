from django.db import models

# Create your models here.


class Team(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=1024)
    tag = models.CharField(max_length=20, blank=True, null=True)


class Player(models.Model):
    STATUS = (
        ('Primary', 'Primary'),
        ('Sub', 'Sub'),
        ('Ineligible', 'Ineligible'),
    )
    name = models.CharField(max_length=1024)
    full_name = models.CharField(max_length=1024)
    team = models.ForeignKey(Team, blank=True, null=True)
    status = models.CharField(
        choices=STATUS,
        default='Primary',
        max_length=1024,
    )
    country = models.CharField(max_length=4, null=True, blank=True)
    rank = models.IntegerField(null=True, blank=True)
    mmr = models.IntegerField(null=True, blank=True)
    updated = models.DateTimeField(blank=True, null=True)