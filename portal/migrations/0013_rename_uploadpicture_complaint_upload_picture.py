# Generated by Django 3.2.5 on 2021-07-17 21:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0012_complaint_uploadpicture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='complaint',
            old_name='uploadpicture',
            new_name='upload_picture',
        ),
    ]