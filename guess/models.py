from django.db import models
from django.core import validators


class GuessResult(models.Model):
    previous_page_path = models.CharField(
        blank=False,
        null=False,
        max_length=500,
    )

    page_path = models.CharField(
        blank=False,
        null=False,
        max_length=500,
    )

    page_view_percent = models.DecimalField(
        max_digits=18,
        decimal_places=15,
        blank=False,
        null=False,
        default=0.000000000000000,
        validators=[
            validators.MinValueValidator(0.000000000000001),
            validators.MaxValueValidator(100.000000000000000)]
        )

    page_views = models.IntegerField(
            blank=False,
            null=False,
            default=0,
            validators=[validators.MinValueValidator(0)]
    )

    class Meta:
        unique_together = (
            ('previous_page_path', 'page_path'),
        )
