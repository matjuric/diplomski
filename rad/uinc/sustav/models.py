from django.db import models
from sympy import false

# class Expertise(models.Model):
#     choices =  (
#         ('ssysadmin', 'Senior System Administrator'),
#         ('jsysadmin', 'Junior System Administrator'),
#         ('scybersec', 'Senior Cyber Security Engineer'),
#         ('jcybersec', 'Junior Cyber Security Engineer'),
#         ('sreveng', 'Senior Reverse Engineer'),
#         ('jreveng', 'Junior Reverse Engineer')
#     )
#     experts = models.CharField(max_length=20, choices=choices)

class Incident(models.Model):
    name = models.CharField('Name', max_length=100)
    spotted_by = models.CharField('Spotted by',max_length=30)
    date_spotted = models.DateTimeField('Date spotted', null=True)

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
    needed_expertise = models.CharField('Needed expertise', max_length=150, default='', null=True)

    # EXPERTISE = (
    #     ('ssysadmin', 'Senior System Administrator'),
    #     ('jsysadmin', 'Junior System Administrator'),
    #     ('scybersec', 'Senior Cyber Security Engineer'),
    #     ('jcybersec', 'Junior Cyber Security Engineer'),
    #     ('sreveng', 'Senior Reverse Engineer'),
    #     ('jreveng', 'Junior Reverse Engineer')
    # )
    # needed_expertise = models.ForeignKey(Expertise, blank=True, on_delete=models.CASCADE, default=None)

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
