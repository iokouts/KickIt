# Generated by Django 2.0.9 on 2018-12-22 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitesettings', '0004_socialmediasettings_fb_app_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmediasettings',
            name='fb_app_id',
            field=models.CharField(blank=True, default='', help_text='Facebook App ID', max_length=255, verbose_name='Facebook App ID'),
        ),
    ]
