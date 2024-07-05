from django.contrib import admin
from .models import Arriendo

@admin.register(Arriendo)
class ArriendoAdmin(admin.ModelAdmin):
    list_display = ('user', 'bike_model', 'start_date', 'end_date', 'price')
    search_fields = ('user__username', 'bike_model')

# Register your models here.
