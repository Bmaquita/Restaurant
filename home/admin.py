from django.contrib import admin

# Register your models here.
from .models import Sliders, OurStory, Testimonials, Gallery, Services

admin.site.register([Sliders, OurStory, Testimonials, Gallery, Services])