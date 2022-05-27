from django.db import models

class Incident(models.Model):
    name = models.CharField(max_length=100)
    spotted_by = models.CharField(max_length=30)
    date_spotted = models.DateTimeField('date spotted', null=True)

    SEVERITIES = (
        ('L', 'low'),
        ('M', 'medium'),
        ('H', 'high')
    )
    severity = models.CharField(max_length=1,choices=SEVERITIES, default='low')

    RESOLVED_OPTIONS = (
        ('Y', 'yes'),
        ('N', 'no')
    )
    resolved = models.CharField(max_length=1, choices=RESOLVED_OPTIONS, default='no')

    def __str__(self) -> str:
        rv = self.name + '\n'
        return rv
    

