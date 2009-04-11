from django.db import models

class Domain(models.Model):
    domain = models.CharField(max_length=255)

    def __unicode__(self):
        return u"%s" % self.domain

class Registrar(models.Model):
    name = models.CharField(max_length=255, blank=True)
    url = models.CharField(max_length=255, blank=True)
    backup_url = models.CharField(max_length=255, blank=True)
    username = models.CharField(max_length=255, blank=True)
    password = models.CharField(max_length=255, blank=True)

    def __unicode__(self):
        return u"%s" % self.name

class Host(models.Model):
    name = models.CharField(max_length=255, blank=True)
    url = models.CharField(max_length=255, blank=True)
    backup_url = models.CharField(max_length=255, blank=True)
    username = models.CharField(max_length=255, blank=True)
    password = models.CharField(max_length=255, blank=True)    

    def __unicode__(self):
        return u"%s" % self.name

class DomainRegistration(models.Model):
    domain = models.ForeignKey(Domain, unique=True)
    registrar = models.ForeignKey(Registrar)
    starts = models.CharField(max_length=255, blank=True)
    expires = models.CharField(max_length=255, blank=True)
    active = models.BooleanField(default=True)
    keep_active = models.BooleanField(default=True)    

    def __unicode__(self):
        return u"%s Registration" % self.domain

    class Meta:
        ordering = ['expires']
        verbose_name_plural = 'Domain Registration Records'

class DomainHosting(models.Model):
    domain = models.ForeignKey(Domain, unique=True)
    host = models.ForeignKey(Host)
    starts = models.CharField(max_length=255, blank=True)
    expires = models.CharField(max_length=255, blank=True)
    active = models.BooleanField(default=True)
    keep_active = models.BooleanField(default=True)

    def __unicode__(self):
        return u"%s Hosting" % self.domain

    class Meta:
        ordering = ['expires']
        verbose_name_plural = 'Domain Hosting Records'

