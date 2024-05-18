from django.contrib import admin

from gymapp import models

# Register your models here.
admin.site.register(models.Instructor)
admin.site.register(models.Physician)
admin.site.register(models.Customer)

# admin.site.register(models.FirstAid)
admin.site.register(models.CustMembership)
admin.site.register(models.CustomerDoubts)
admin.site.register(models.CustomerComplaint)
admin.site.register(models.GymServices)


admin.site.register(models.Membership)
admin.site.register(models.HealthDetails)
admin.site.register(models.Fee)
