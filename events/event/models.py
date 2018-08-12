from django.db import models


class Event(models.Model):

    CONFERENCE = 'Conference'
    SEMINAR = 'Seminar'
    CONGRESS = 'Congress'
    COURSE = 'Course'

    CATEGORY_CHOICES = (
        (CONFERENCE, 'Conference'),
        (SEMINAR, 'Seminar'),
        (CONGRESS, 'Congress'),
        (COURSE, 'Course')
    )

    FACE = 'Face-to-face'
    VIRTUAL = 'Virtual'

    CLASSIFICATION_CHOICES = (
        (FACE, 'Face-to-face'),
        (VIRTUAL, 'Virtual')
    )

    name = models.CharField(max_length=200,null=True,blank=True)
    vanue = models.CharField(max_length=200,null=True,blank=True)
    address = models.CharField(max_length=200,null=True,blank=True)
    start_date = models.DateTimeField(null=True,blank=True)
    end_date = models.DateTimeField(null=True,blank=True)
    category = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES,
        default=CONGRESS
    )
    classification = models.CharField(
        max_length=100,
        choices=CLASSIFICATION_CHOICES,
        default=FACE
    )