# Generated by Django 5.1.6 on 2025-03-06 14:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_category_customer_product_description_product_image_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
    ]
