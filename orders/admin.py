from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Category)
admin.site.register(Regular_pizza)
admin.site.register(Sicilian_pizza)
admin.site.register(Pizza_toppingR)
admin.site.register(Pizza_toppingS)
admin.site.register(Topping)
admin.site.register(Sub)
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(Dinner_platter)
admin.site.register(Orders)
admin.site.register(Order_counter)