from django.contrib import admin
from .models import Land, House, Agent, property_reviews

# Register your models here.
admin.site.register(Land)
admin.site.register(House)
admin.site.register(Agent)
admin.site.register(property_reviews)
