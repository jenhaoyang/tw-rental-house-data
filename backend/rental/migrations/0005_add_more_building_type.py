# Generated by Django 2.0.7 on 2018-08-24 01:54

from django.db import migrations, models
import rental.enums


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0004_fill_crawled_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='building_type',
            field=models.IntegerField(choices=[(rental.enums.BuildingType(0), 0), (rental.enums.BuildingType(1), 1), (rental.enums.BuildingType(2), 2), (rental.enums.BuildingType(3), 3), (rental.enums.BuildingType(4), 4), (rental.enums.BuildingType(5), 5), (rental.enums.BuildingType(6), 6), (rental.enums.BuildingType(7), 7), (rental.enums.BuildingType(8), 8), (rental.enums.BuildingType(9), 9)], null=True),
        ),
        migrations.AlterField(
            model_name='housets',
            name='building_type',
            field=models.IntegerField(choices=[(rental.enums.BuildingType(0), 0), (rental.enums.BuildingType(1), 1), (rental.enums.BuildingType(2), 2), (rental.enums.BuildingType(3), 3), (rental.enums.BuildingType(4), 4), (rental.enums.BuildingType(5), 5), (rental.enums.BuildingType(6), 6), (rental.enums.BuildingType(7), 7), (rental.enums.BuildingType(8), 8), (rental.enums.BuildingType(9), 9)], null=True),
        ),
    ]