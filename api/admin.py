from django.contrib import admin

from .models import WhiteUser, AlienUser


# Register your models here.
@admin.register(WhiteUser)
class WhiteUserAdmin(admin.ModelAdmin):
    list_display = ['username']


@admin.register(AlienUser)
class AlienUserAdmin(admin.ModelAdmin):
    list_display = ['username']
