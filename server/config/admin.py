from django.contrib import admin
from apps.comics.models import Comic
from apps.reviews.models import Review

# Register your models here.
admin.site.register(Comic)
admin.site.register(Review)