# Generated by Django 4.2.15 on 2024-08-29 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digi', '0002_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='media/default.jpg', upload_to=''),
        ),
    ]
