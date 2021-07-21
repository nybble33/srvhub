# -*- coding: utf-8 -*-

from django.db import models
import datetime

# Create your models here.


class Web_Page (models.Model):
    STATUS_CHOICES = (
        (0, 'In progress'),
        (1, 'Completed'),
    )
    modified = models.DateTimeField(
        'Date of creation or modifying',
        default=datetime.datetime.now
            )
    url = models.CharField('URL of page for parsing', max_length=255)
    token = models.SlugField('Request TOKEN', unique=True)
    results = models.TextField('Request results', null=True, blank=True)
    status = models.IntegerField(
        'Status',
        choices=STATUS_CHOICES,
        default=0
        )

    class Meta:
        ordering = ['modified']
