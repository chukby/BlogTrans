from django.contrib import admin
from .models import Post

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'status', 'date_created')
    list_filter = ('status', 'date_created')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title', )}
    raw_id_fields = ('author', )
    date_hierarchy = 'date_created'
    ordering = ('status', 'date_created')


admin.site.register(Post, PostAdmin)
