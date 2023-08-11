from django.contrib import admin

# Register your models here.

from .models import Category, Meal

@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):

     prepopulated_fields={
        'slug':('name',)
    }


admin.site.register([Category])
