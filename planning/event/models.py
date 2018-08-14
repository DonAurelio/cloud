from django.db import models
from django.urls import reverse
from django import forms
from django.core.exceptions import ValidationError

from authentication.models import Account
import datetime
import pytz

now = datetime.datetime.now()


def validate_star_date(start_date):
    """Validate start date."""
    now = datetime.datetime.now()

    # Now datetime is naive, so it is localized
    # to the current user timezone.
    now_aware = pytz.utc.localize(now)

    if start_date < now_aware:
        raise ValidationError(
            'Start date %(start)s must be greater than current time %(now)s',
            params={
                'start': start_date,
                'now': now_aware
            },
        )


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
    name = models.CharField(max_length=200)
    venue = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    start_date = models.DateTimeField(
        validators=[validate_star_date],
        help_text="Please use the following format: YYYY-MM-DD HH:MM:ss. e.g, 2018-08-14 22:10:24."
    )
    end_date = models.DateTimeField(
        help_text="Please use the following format: YYYY-MM-DD HH:MM:ss. e.g, 2018-08-14 22:11:00."
    )
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
        """This method is needed for the class based views Create and Update."""
        return reverse('event:detail', kwargs={'pk': self.pk})

    def clean(self):
        """Check if start_date is lower than end_date."""
        super(Event, self).clean()
        if self.start_date >= self.end_date:
            raise forms.ValidationError('Start date must be less than the End date.')