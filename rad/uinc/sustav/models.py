from django.db import models
from sympy import false

class Incident(models.Model):
    name = models.CharField('Name', max_length=100)
    spotted_by = models.CharField('Spotted by',max_length=30)
    date_spotted = models.DateTimeField('Date spotted', null=True, help_text="Expected format: <b>YYYY-MM-DD HH:MM:SS<b>", blank=True)

    SEVERITIES = (
        ('L', 'low'),
        ('M', 'medium'),
        ('H', 'high')
    )
    severity = models.CharField('Severity', max_length=1,choices=SEVERITIES, default='low')

    RESOLVED_OPTIONS = (
        ('N', 'no'),
        ('Y', 'yes')
    )
    resolved = models.CharField('Resolved', max_length=1, choices=RESOLVED_OPTIONS, default='no')

    beggining = models.CharField('Beggining', max_length=100, default='', null=True)
    name_sender = models.CharField('Name / Sender', max_length=100, default='', null=True)
    ending_title = models.CharField('Ending / Title', max_length=100, default='', null=True)
    initiator_receiver = models.CharField('Initiator / Receiver', max_length=100, default='', null=True)
    parameters_textmsg = models.CharField('Parameters / Text Message', max_length=100, default='', null=True)
    content = models.TextField('Content', max_length=300, default='', null=True, blank=True)
    needed_expertise = models.CharField('Needed expertise', max_length=150, default='', blank=True, null=True, help_text="Entered comma-separated text. Example: <b>sysadmin,devops,reverseengineer<b>")
    # upload_xlsx = models.FileField('Upload XLSX file', upload_to='.', default='', blank=True)

    def __str__(self) -> str:
        rv = self.name + '\n'
        return rv
    
    def get_field_values(self):
        return [ (field.verbose_name, field.value_from_object(self)) for field in Incident._meta.get_fields() ]
    
    def has_expertise(self):
        if (self.needed_expertise == ''):
            return False
        return True

    def get_needed_expertise(self):
        return [ expertise for expertise in self.needed_expertise.split(',') ]
