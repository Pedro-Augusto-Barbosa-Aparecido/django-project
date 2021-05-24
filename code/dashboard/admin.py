from django.contrib import admin

from dashboard.models import Sensor, UsersSystem, Value

admin.site.register(Sensor)
admin.site.register(UsersSystem)
admin.site.register(Value)
