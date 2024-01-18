from django.contrib import admin

from blog.models import Category, Post


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'author', 'published','post_categories') #columnas a desplegar
    ordering = ('author', 'published')
    search_fields = ('title', 'content', 'author__username', 'categories__name')            #campos de busqueda
    date_hierarchy = 'published'
    list_filter = ('author__username', 'published', 'categories')
    # prepopulated_fields = {'slug': ('title',)}

    def post_categories(selfs, obj):
        return ", ".join([ c.name for c in obj.categories.all().order_by('name')])

    post_categories.short_description = 'Categorías'

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post,PostAdmin)