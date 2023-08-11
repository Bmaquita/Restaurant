from django.contrib import admin

# Register your models here.
from . models import Post, Category

@admin.register(Post)
class PostsAdmin(admin.ModelAdmin):

    prepopulated_fields ={
        'slug':('title',)
    }


admin.site.register(Category)