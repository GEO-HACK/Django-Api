from django.contrib import admin
from .models import Drinks #avoid importing all for cleaner code 


admin.site.register(Drinks)
