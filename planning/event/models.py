from django.db import models
from django.urls import reverse

from authentication.models import Account

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

    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200,null=True,blank=True)
    venue = models.CharField(max_length=200,null=True,blank=True)
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
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Order event objects by desending
        ordering = ['-created_at']


    def get_absolute_url(self):
        return reverse('event:detail', kwargs={'pk': self.pk})