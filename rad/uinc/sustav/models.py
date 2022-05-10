from django.db import models

from taggit.managers import TaggableManager

class Incident(models.Model):
    name = models.CharField(max_length=100)
    spotted_by = models.CharField(max_length=30)
    # date_spotted = models.DateTimeField('date spotted')
    # severity = models.NESTO
    tags = TaggableManager() # mozda nakaciti severity na ovo

    def __str__(self) -> str:
        rv = self.name + '\n'
        rv += 'Spotted by: ' + self.spotted_by + '\n'
        # rv += self.date_spotted
        return rv
    

