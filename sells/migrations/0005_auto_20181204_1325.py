# Generated by Django 2.1.1 on 2018-12-04 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sells', '0004_auto_20181204_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='gold',
            field=models.CharField(db_index=True, max_length=100),
        ),
    ]
