from django.contrib import admin
from django.contrib.auth.models import User, Group

from django_domains.domains.models import Domain, Registrar, Host, DomainRegistration, DomainHosting
from django_domains.domains.admin import DomainAdmin, RegistrarAdmin, HostAdmin, DomainRegistrationAdmin, DomainHostingAdmin

class AdminSite(admin.AdminSite):
    pass

site = AdminSite()

# site.register(User)
# site.register(Group)

site.register(Domain, DomainAdmin)
site.register(Registrar, RegistrarAdmin)
site.register(Host, HostAdmin)
site.register(DomainRegistration, DomainRegistrationAdmin)
site.register(DomainHosting, DomainHostingAdmin)

