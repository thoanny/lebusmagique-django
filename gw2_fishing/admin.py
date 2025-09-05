from django.utils.html import format_html
from django.contrib import admin
from .models import Fish, Achievement, Bait, Hole, FishHole, Time, Daily


class BaitAdmin(admin.ModelAdmin):
    list_display = ['item_name', 'power']
    search_fields = ['item__name']
    autocomplete_fields = ['item']
    ordering = ('item__name',)

    def item_name(self, obj):
        return obj.item.name
    item_name.admin_order_field = 'item__name'


class FishHoleInline(admin.TabularInline):
    model = FishHole
    extra = 0
    can_delete = True


class TimeInline(admin.TabularInline):
    model = Time
    extra = 0
    can_delete = True


class FishAdmin(admin.ModelAdmin):
    list_display = ['item_name', 'thumbnail', 'power_min', 'power_max', 'bait', 'achievement', 'daily_catch']
    list_filter = ['achievement', 'daily_catch']
    search_fields = ['item__name']
    autocomplete_fields = ['item', 'bait']
    ordering = ('item__name',)
    inlines = [FishHoleInline, TimeInline]

    def thumbnail(self, obj):
        print(obj)
        if obj.item.icon:
            return format_html('<a href="{}" target="_blank"><img src="{}" height="28px" /></a>', obj.item.icon, obj.item.icon)
        return "-"
    thumbnail.short_description = "Image"

    def item_name(self, obj):
        return obj.item.name
    item_name.admin_order_field = 'item__name'



class AchievementAdmin(admin.ModelAdmin):
    list_display = ['name', 'achievement_id', 'repeat_achievement_id']
    ordering = ('name',)


class HoleAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ('name',)


class DailyAdmin(admin.ModelAdmin):
    list_display = ['date', 'arborstone', 'lowland_shore', 'janthir_syntri', 'mistburned_barrens']
    list_filter = ['date']
    autocomplete_fields = ['arborstone', 'lowland_shore', 'janthir_syntri', 'mistburned_barrens']
    ordering = ('-date',)


admin.site.register(Achievement, AchievementAdmin)
admin.site.register(Bait, BaitAdmin)
admin.site.register(Hole, HoleAdmin)
admin.site.register(Fish, FishAdmin)
admin.site.register(Daily, DailyAdmin)
