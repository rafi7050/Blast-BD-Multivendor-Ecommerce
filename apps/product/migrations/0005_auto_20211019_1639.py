# Generated by Django 3.1.6 on 2021-10-19 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20211019_1618'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_2',
            field=models.ImageField(blank=True, default='https://via.placeholder.com/240x180.jpg', null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_3',
            field=models.ImageField(blank=True, default='https://via.placeholder.com/240x180.jpg', null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_4',
            field=models.ImageField(blank=True, default='https://via.placeholder.com/240x180.jpg', null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_5',
            field=models.ImageField(blank=True, default='https://via.placeholder.com/240x180.jpg', null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_6',
            field=models.ImageField(blank=True, default='https://via.placeholder.com/240x180.jpg', null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_7',
            field=models.ImageField(blank=True, default='https://via.placeholder.com/240x180.jpg', null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_8',
            field=models.ImageField(blank=True, default='https://via.placeholder.com/240x180.jpg', null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='thumbnail',
            field=models.ImageField(blank=True, default='https://via.placeholder.com/240x180.jpg', null=True, upload_to='uploads/'),
        ),
    ]
