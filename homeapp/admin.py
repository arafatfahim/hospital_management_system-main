from django.contrib import admin

from homeapp.models import Department,Laboratory,Ambulance,services,Review,Gallery

admin.site.register(Department)
admin.site.register(Laboratory)
admin.site.register(Ambulance)
admin.site.register(services)
admin.site.register(Review)
admin.site.register(Gallery)
