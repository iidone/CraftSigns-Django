from django.contrib import admin
from .models import Production
from .models import OurWorks
from .models import Services

admin.site.register(Production)
admin.site.register(OurWorks)
admin.site.register(Services)
