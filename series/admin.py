# Django
from django.contrib import admin

# Models
from series.models import Series, Episodes

# Register your models here.

@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'state', 'banner_state')
    list_display_links = ('name',)
    list_filter = (
        'state', 'created'
    )
    search_fields = (
        'pk', 'name',
        'state'
    )

    fieldsets = (
        ('Main information', {
            'fields': (
                ('name', 'state'),
                ('slug')
            )
        }),

        ('Picture publication', {
            'fields': (
                ('picture', 'picture_banner', 'banner_state'), 
            )
        }),

        ('Additional inforamtion', {
            'fields': (
                ('sinopsis',),
            )
        }),

        ('Metadata', {
            'fields': (('created', 'modified'),),
        })
    )

    list_editable = ('state', 'banner_state')
    readonly_fields = ('created', 'modified')

@admin.register(Episodes)
class EpisodesAdmin(admin.ModelAdmin):
    list_display = ('episode','name', 'serie','URL_video')
    list_display_links = ('episode', 'name', 'serie')
    list_filter = (
        'serie', 
        'modified', 'created'
    )
    search_fields = (
        'pk', 'name',
        'episode',
    )

    fieldsets = (
        ('Main information', {
            'fields': (
                ( 'serie', 'episode'), 
                ('name', 'slug')
            )
        }),
        ('Video URL', {
            'fields': (
                ('URL_video'),
            )
        }),
        ('Additional inforamtion', {
            'fields': (
                ('sinopsis'),
            )
        }),
        ('Metadata', {
            'fields': (('created', 'modified'),),
        })
    )

    list_editable = ('URL_video',)
    readonly_fields = ('created', 'modified')