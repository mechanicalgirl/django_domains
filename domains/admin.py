from django.contrib import admin

from domains.models import Domain, Registrar, Host, DomainRegistration, DomainHosting

class DomainAdmin(admin.ModelAdmin):
    list_display = ('domain',)

class RegistrarAdmin(admin.ModelAdmin):
    list_display = ('name',)

class HostAdmin(admin.ModelAdmin):
    list_display = ('name',)

class DomainRegistrationAdmin(admin.ModelAdmin):
    list_display = ('domain', 'registrar', 'expires', 'active', 'keep_active',)

class DomainHostingAdmin(admin.ModelAdmin):
    list_display = ('domain', 'host', 'expires', 'active', 'keep_active',)


