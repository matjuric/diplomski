from django.db import models

from taggit.managers import TaggableManager

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
    # severity = models.NESTO
    # tags = TaggableManager() # mozda nakaciti severity na ovo

    def __str__(self) -> str:
        rv = self.name + '\n'
        rv += 'Spotted by: ' + self.spotted_by + '\n'
        rv += str(self.date_spotted) if self.date_spotted else ''
        rv += ' SEVERITY: ' + self.severity + '\n'
        rv += ' private_key = \n' + str(self.pk)
        return rv
    

