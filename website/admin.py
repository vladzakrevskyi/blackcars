from django_summernote.admin import SummernoteModelAdmin, SummernoteWidget
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import *


class CarRentPeriodInline(admin.TabularInline):
    model = CarRentPeriod
    min_num = 4
    max_num = 4


class OptionInline(admin.TabularInline):
    model = Option


class MainSLiderAdmin(admin.ModelAdmin):
    list_display = ('title', )


class ImagesInline(admin.TabularInline):
    model = SliderImage


class ServiceTabeInline(admin.TabularInline):
    model = ServiceTable
    extra = 1


class ExtraOptionsInline(admin.TabularInline):
    model = ExtraOptions
    extra = 1


class ServicePageAdmin(admin.ModelAdmin):
    inlines = [ServiceTabeInline, ]


class CarAdmin(SummernoteModelAdmin):
    inlines = [CarRentPeriodInline, OptionInline, ImagesInline, ExtraOptionsInline]
    list_display = ('model', 'month_price', 'price', 'promotion', 'my_order', 'show_on_home', 'disable')
    list_editable = ('month_price', 'price', 'promotion', 'my_order', 'show_on_home', 'disable')


class ServiceAdmin(SummernoteModelAdmin):
    summernote_fields = ('__all__')
    list_display = ('title', 'my_order')
    list_editable = ('my_order',)


class CarDetailTablesAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc')
    list_editable = ('desc',)

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('__all__')
    list_display = ('title', 'date')
    list_editable = ('date',)


class SubscriberAdmin(ImportExportModelAdmin):
    list_display = ('email', 'date')


admin.site.register(Post, PostAdmin)
admin.site.register(MainSLider, MainSLiderAdmin)
admin.site.register(RentPeriod)
admin.site.register(Car, CarAdmin)
admin.site.register(ServicePage, ServicePageAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(CarDetailTables, CarDetailTablesAdmin)
