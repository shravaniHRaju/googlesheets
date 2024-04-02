from django.db import models

# Create your models here.
#gsheets

from django.db import models
#from gsheets import mixins
#from uuid import uuid4

#class student(mixins.SheetSyncableMixin, models.Model):
class student( models.Model):
    #spreadsheet_id = '18F_HLftNtaouHgA3fmfT2M1Va9oO-YWTBw2EDsuz8V4'
    #model_id_field = 'guid'

    #guid = models.CharField(primary_key=True, max_length=255, default=uuid4)

    name = models.CharField(max_length=127)
    age = models.CharField(max_length=127)
    address = models.CharField(max_length=127, null=True, blank=True, default=None)


    def __str__(self):
        return f'{self.name}  // {self.age} ({self.address})'
