from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from django.db.models.enums import Choices
from django.db.models.fields import AutoField, BooleanField, CharField, DateField, DateTimeField, EmailField 
import uuid 
# Create your models here.

COLLEGE = 'CLG'
HOSTEL = 'HOS'
SUBMITTED = 'Complaint Has Been Submitted.'
PROGRESS = 'Complaint Is Under Progress.'
RESOLVED = 'Your Complaint Has Been Resolved.'

class Complaint(models.Model):
    complaintnumber = models.UUIDField(default=uuid.uuid4)
    name = CharField(max_length=25)
    enrollment = CharField(max_length=15)
    department = CharField(max_length=5)
    reg =  [
        (COLLEGE, 'College'),
        (HOSTEL, 'Hostel'),
        ]
    regarding = models.CharField(
        max_length=10,
        choices=reg,
        default=COLLEGE)
    mobile = CharField(max_length=10)
    email = EmailField(max_length=50, null=True)
    detail = CharField(max_length=500)
    image = models.ImageField(upload_to='complaint/')
    stat =  [
        (SUBMITTED, 'Complaint Has Been Submitted.'),
        (PROGRESS, 'Complaint Is Under Progress.'),
        (RESOLVED,'Your Complaint Has Been Resolved.')
        ]
    status = models.CharField(
        max_length=100,
        choices=stat,
        default=SUBMITTED)
    date = DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Complaint'
        verbose_name_plural = 'Complaints'

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = CharField(max_length=30)
    department = CharField(max_length=10)
    mobile = CharField(max_length=10)
    email = EmailField(max_length=30)
    reason = CharField(max_length=100)
    date = DateTimeField(auto_now=True)
    class Meta:
        """Meta definition for contact."""

        verbose_name = 'ContactUs'
        verbose_name_plural = 'contactsUs'

    def __str__(self):
        """Unicode representation of contact."""
        return self.reason
