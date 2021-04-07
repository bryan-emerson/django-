from django.contrib import admin

# Register your models here.
from .models import Artist
from .models import Album
admin.site.register(Artist)
admin.site.register(Album)
