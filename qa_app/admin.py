from django.contrib import admin
from .models import *
# Register your models here.

class subadmin(admin.ModelAdmin):
    prepopulated_fields={"slug":("sub_name",)}

admin.site.register(subject,subadmin)

admin.site.register(syllabus)


admin.site.register(Qa)
