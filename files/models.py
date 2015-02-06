import datetime

from django.db import models


def created():
    """ Returns the current time."""
    return datetime.datetime.now()


def expires():
    """
        Returns the expiration time,
        which is calculated as current time tomorrow
    """
    return datetime.datetime.now() + datetime.timedelta(days=1)


class Token(models.Model):
    """Token model which represents an expirable key to file encryption"""
    created = models.DateTimeField('Creation date', default=created)
    expires = models.DateTimeField('Expiration date', default=expires)
    key = models.CharField(max_length=200)

    def __unicode__(self):
        return self.key


class File(models.Model):
    """File model which encaplusates file information"""
    url = models.CharField(max_length=200)
    path = models.CharField(max_length=200)
    name = models.CharField(max_length=50)
    created = models.DateTimeField('Creation date', default=created)
    token = models.ForeignKey(Token)

    def __unicode__(self):
        return self.name

