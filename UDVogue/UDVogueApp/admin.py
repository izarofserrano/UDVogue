from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Editorial, Revista, Producto

admin.site.register(Editorial)
admin.site.register(Revista)
admin.site.register(Producto)