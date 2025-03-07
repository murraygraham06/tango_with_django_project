from django.contrib import admin
from rango.models import Category, Page

#admin.site.register(Category)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)

class ChoiceInline(admin.TabularInline):
    model = Category
    extra = 3

class PageAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title', {'fields': ['title']}),
        ('Category', {'fields': ['category']}),
        ('URL', {'fields': ['url'], 'classes': ['collapse']}),
    ]
    list_display = ( 'title', 'category', 'url')

admin.site.register(Page, PageAdmin)