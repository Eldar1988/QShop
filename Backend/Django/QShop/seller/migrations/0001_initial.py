# Generated by Django 3.2.3 on 2021-05-14 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('user_id', models.CharField(db_index=True, max_length=255)),
                ('phone', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=12)),
                ('mailing', models.BooleanField(default=False)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='seller/avatars/')),
                ('register_date', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-register_date',),
            },
        ),
        migrations.CreateModel(
            name='Tariff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=350)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('register_date', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('amount',),
            },
        ),
        migrations.CreateModel(
            name='SellerShop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255)),
                ('description', models.TextField()),
                ('logo', models.ImageField(blank=True, null=True, upload_to='seller/logos/')),
                ('favicon', models.ImageField(blank=True, null=True, upload_to='seller/favicons/')),
                ('url', models.CharField(blank=True, max_length=255, null=True)),
                ('register_date', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shops', to='seller.seller')),
            ],
            options={
                'ordering': ('-register_date',),
            },
        ),
        migrations.AddField(
            model_name='seller',
            name='tariff',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sellers', to='seller.tariff'),
        ),
    ]
