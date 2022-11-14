from django.db import models


# Create your models here.

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=100)
    user_password = models.CharField(max_length=100)
    user_address = models.CharField(max_length=100)
    user_tel = models.CharField(max_length=100)
    user_icon = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'user'


class Food(models.Model):
    food_id = models.AutoField(primary_key=True)
    food_name = models.CharField(max_length=100, blank=True, null=True)
    food_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    food_store = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'food'


class FoodEvaluate(models.Model):
    food_evaluate_id = models.AutoField(primary_key=True)
    food_evaluate_text = models.CharField(max_length=100, blank=True, null=True)
    food_evaluate_score = models.IntegerField(blank=True, null=True)
    food = models.ForeignKey(Food, models.DO_NOTHING, blank=True, null=True)
    post_user = models.ForeignKey('User', models.DO_NOTHING)
    food_evaluate_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'food_evaluate'


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_completed = models.IntegerField()
    order_user = models.ForeignKey('User', models.DO_NOTHING, related_name='order_user_1')
    delivery_user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True, related_name='order_user_2')
    order_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order'


