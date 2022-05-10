from django.contrib import admin
from .models import ( 
    Hero,
    ServiceChart,
    About,
    Services,
    Team,
    Gallery,
    RoomsRates,
    Visitors,
    saveContact,
    saveChecking,
    bookingList,
    booking,
    )

# Register your models here.

@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ('name', 'tag', 'greet', 'is_active')


@admin.register(ServiceChart)
class ServiceChartAdmin(admin.ModelAdmin):
    list_display = ('name', 'company_name', 'icon')


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('image_one', 'image_two', 'heading', 'description', 'offer', 'offer_description')


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('heading', 'description', 'is_active')


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation', 'image', 'is_active')


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'is_active')

@admin.register(RoomsRates)
class RoomsRatesAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image', 'is_active')


@admin.register(Visitors)
class VisitorsAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'title', 'is_active')


@admin.register(saveContact)
class saveContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')


@admin.register(saveChecking)
class saveCheckingAdmin(admin.ModelAdmin):
    list_display = ('roomtype', 'adate', 'ddate')

@admin.register(bookingList)
class bookingListAdmin(admin.ModelAdmin):
    list_display = ('room_type', 'check_in', 'check_out')

@admin.register(booking)
class bookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'number', 'room_price', 'check_in', 'check_out')