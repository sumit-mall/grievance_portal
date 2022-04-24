# Generated by Django 3.2.5 on 2021-08-06 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0034_alter_complaint_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complaint',
            name='image',
        ),
        migrations.AddField(
            model_name='complaint',
            name='photo_img',
            field=models.ImageField(default='articles/default.jpg', upload_to='articles/'),
        ),
    ]