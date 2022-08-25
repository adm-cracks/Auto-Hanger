from django.contrib import admin
from .models import brands
from .models import parts

# Register your models here.

admin.site.register(brands)
admin.site.register(parts)