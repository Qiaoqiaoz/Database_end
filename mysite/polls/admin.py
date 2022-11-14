from django.contrib import admin

# Register your models here.
#导入模型User,Article
from .models import User,Food,FoodEvaluate,Order

admin.site.register(User)
admin.site.register(Food)
admin.site.register(FoodEvaluate)
admin.site.register(Order)
