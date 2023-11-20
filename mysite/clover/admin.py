from django.contrib import admin

from .models import Account, AccountProfile, Person, PersonProfile, Brand, BrandProfile, Domain, DomainProfile, Location, LocationProfile, PersonAccount

admin.site.register(Account)
admin.site.register(AccountProfile)
admin.site.register(Person)
admin.site.register(PersonProfile)
admin.site.register(Brand)
admin.site.register(BrandProfile)
admin.site.register(Location)
admin.site.register(LocationProfile)
admin.site.register(Domain)
admin.site.register(DomainProfile)
admin.site.register(PersonAccount)