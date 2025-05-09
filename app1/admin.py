from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(New)
class NewAdmin(admin.ModelAdmin):
    search_fields = ['title','short_desc','desription']
    list_per_page = 20
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']
    list_display = ['name', 'slug']
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email','is_trash','is_read']
