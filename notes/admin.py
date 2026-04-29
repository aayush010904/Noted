from django.contrib import admin
from . import models
# Register your models here.


class NotesAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created')
    search_fields = ('title', 'text', 'tags__name')
    list_filter = ('created', 'tags')
    filter_horizontal = ('tags',)


class TagAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('name',)

admin.site.register(models.Notes, NotesAdmin)
admin.site.register(models.Tag, TagAdmin)