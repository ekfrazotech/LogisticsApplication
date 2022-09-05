from django.contrib import admin

# Register your models here.
from .models import *
# from import_export.admin import ImportExportModelAdmin

model_list = [  
    
    City,
    CustomUser,
    VehicleTypes,
    Vehicle,
    Review,
    Driver,
    CustomerAddress,
    PickupDetails,
    DropDetails,
    PlacedOrder,
    Coupons,
    Status,
    InOrder, 
]

admin.site.register(model_list)



class AdminUserRoleRef(admin.ModelAdmin):
    list_display = ('user_role_name','create_timestamp','last_update_timestamp')

admin.site.register(UserRoleRef,AdminUserRoleRef)

