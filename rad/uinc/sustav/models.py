from unittest.util import _MAX_LENGTH
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

    beggining = models.CharField(max_length=100, default='', null=True)
    name_sender = models.CharField(max_length=100, default='', null=True)
    ending_title = models.CharField(max_length=100, default='', null=True)
    initiator_receiver = models.CharField(max_length=100, default='', null=True)
    parameters_textmsg = models.CharField(max_length=100, default='', null=True)
    content = models.TextField(max_length=300, default='', null=True)

    def __str__(self) -> str:
        rv = self.name + '\n'
        return rv
    

# Beginning	Name / Sender	Ending / Title	Initiator / Receiver	Parameters / Text Message	Content
#1# 7/1/2022 3:02
#2#	Recon	
#3# Recon: 'Attacker' discovered a new person: SPI IT technican 01
#4# 	APT Grupa	
#5# 'Attacker' discovered a new person: SPI IT technican 01
#6# 	'Attacker' discovered a new person: SPI IT technican 01


#1# 7/1/2022 18:31
#2# 	Create Spearphishing Mail With Link
#3# 7/1/2022 18:31
#4# APT Grupa
#5#	Actor: Attacker Target: SRPI Zaposlenik 02 Phishing application: Webmail SquirrelMail Popular Forum Mail Subject: Etherum Sale
