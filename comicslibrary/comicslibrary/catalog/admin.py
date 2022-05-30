from django.contrib import admin

from .models import Genre, Comic, Publisher

admin.site.register(Genre)

@admin.register(Comic)
class ComicAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'display_genre')
    list_filter = ('status', 'year')

class ComicInline(admin.TabularInline):
    model = Comic

@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
	inlines = [ComicInline]