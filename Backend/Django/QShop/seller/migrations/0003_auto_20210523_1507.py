# Generated by Django 3.2.3 on 2021-05-23 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0002_alter_seller_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='tariff',
            field=models.DecimalField(decimal_places=2, default=130, max_digits=12),
        ),
        migrations.DeleteModel(
            name='Tariff',
        ),
    ]
