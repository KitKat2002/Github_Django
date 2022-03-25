from django.db import models

# Create your models here.

from django.db import models

# Create your mo
class DjangoClasses(models.Model):
    Title = models.CharField(max_length=60, default="", blank=True, null=False)
    Course_Number = models.IntegerField(default="1", blank=False, null=False)
    Instructor_Name = models.CharField(max_length=60, default="", blank=True, null=False)
    Duration_weeks = models.FloatField(default="1.5", blank=False, null=False)

objects = models.Manager()

def __str__(self):
    return self.name