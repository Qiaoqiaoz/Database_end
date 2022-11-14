# Generated by Django 4.1 on 2022-09-18 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('food_id', models.AutoField(primary_key=True, serialize=False)),
                ('food_name', models.CharField(blank=True, max_length=100, null=True)),
                ('food_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10)),
                ('food_store', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
