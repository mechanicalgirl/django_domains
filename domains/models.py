from django.db import models

class Domain(models.Model):
    domain = models.CharField(max_length=255)

    def __str__(self):
        return self.domain

class Registrar(models.Model):
    name = models.CharField(max_length=255, blank=True)
    url = models.CharField(max_length=255, blank=True)
    backup_url = models.CharField(max_length=255, blank=True)
    username = models.CharField(max_length=255, blank=True)
    password = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

class Host(models.Model):
    name = models.CharField(max_length=255, blank=True)
    url = models.CharField(max_length=255, blank=True)
    backup_url = models.CharField(max_length=255, blank=True)
    username = models.CharField(max_length=255, blank=True)
    password = models.CharField(max_length=255, blank=True)    

    def __str__(self):
        return self.name

class DomainRegistration(models.Model):
    domain = models.ForeignKey(Domain, unique=True)
    registrar = models.ForeignKey(Registrar)
    starts = models.CharField(max_length=255, blank=True)
    expires = models.CharField(max_length=255, blank=True)
    active = models.BooleanField(default=True)
    keep_active = models.BooleanField(default=True)    

    def __str__(self):
        return "%s Registration" % self.domain

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

    def __str__(self):
        return "%s Hosting" % self.domain

    class Meta:
        ordering = ['expires']
        verbose_name_plural = 'Domain Hosting Records'

