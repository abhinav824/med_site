from django.contrib import admin
from med.models import *
#Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    pass

class SupplierAdmin(admin.ModelAdmin):
    pass

class RetailerAdmin(admin.ModelAdmin):
    pass

class DistributorAdmin(admin.ModelAdmin):
    pass

class stockAdmin(admin.ModelAdmin):
    pass

class medicineAdmin(admin.ModelAdmin):
    pass

class OrderAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(Supplier,SupplierAdmin)
admin.site.register(Retailer,RetailerAdmin)
admin.site.register(Distributor,DistributorAdmin)
admin.site.register(stock,stockAdmin)
admin.site.register(medicine,medicineAdmin)
admin.site.register(Order,OrderAdmin)
