# Generated by Django 2.0.9 on 2018-12-22 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitesettings', '0003_auto_20181108_2101'),
    ]

    operations = [
        migrations.AddField(
            model_name='socialmediasettings',
            name='fb_app_id',
            field=models.CharField(blank=True, help_text='Facebook App ID', max_length=255),
        ),
    ]
