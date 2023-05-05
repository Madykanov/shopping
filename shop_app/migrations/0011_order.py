# Generated by Django 4.2 on 2023-05-04 05:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop_app', '0010_cart_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=100, null=True, verbose_name='Product')),
                ('size', models.IntegerField(default='35', null=True, verbose_name='size')),
                ('price', models.FloatField(default='0.00', null=True, verbose_name='price')),
                ('quant', models.IntegerField(default='5', null=True, verbose_name='quant')),
                ('brand', models.CharField(max_length=100, null=True, verbose_name='Brand')),
                ('title', models.CharField(max_length=50, verbose_name='Name product')),
                ('description', models.TextField(verbose_name='description')),
                ('image', models.ImageField(null=True, upload_to='Product_img', verbose_name='image')),
                ('gender', models.CharField(max_length=100, null=True, verbose_name='Gender')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Корзины',
            },
        ),
    ]
