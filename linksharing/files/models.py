from django.db import models


class Token(models.Model):
    created = models.DateTimeField('Creation date')
    expires = models.DateTimeField('Expiration date')
    key = models.CharField(max_length=200)

    def __unicode__(self):
        return self.key


class File(models.Model):
    url = models.CharField(max_length=200)
    path = models.CharField(max_length=200)
    name = models.CharField(max_length=50)
    created = models.DateTimeField('Creation date')
    file = models.FileField(upload_to='documents/%Y/%m/%d')
    token = models.ForeignKey(Token)

    def __unicode__(self):
        return self.name
