from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Rocky_Railway,Roar,Shipwreched,FWN1,FWN2,FWN3,LIFE_OF_JESUS,Friends_with_God_Bible_Story,Product,Category
from . import models

# Register your models here.

#admin.site.register(item)
@admin.register(Rocky_Railway,Roar,Shipwreched,FWN1,FWN2,FWN3,LIFE_OF_JESUS,Friends_with_God_Bible_Story,Product,Category)
class ViewAdmin(ImportExportModelAdmin):
    pass
