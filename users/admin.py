from django.contrib import admin
from .models import Time,Present,UserProfile
from import_export.admin import ImportExportModelAdmin

class timeAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
class presentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
class userProfileAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    ...
# Register your models here.
admin.site.register(Time, timeAdmin)
admin.site.register(Present, presentAdmin)
admin.site.register(UserProfile, userProfileAdmin)