# Generated by Django 3.2.8 on 2021-10-22 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitesettings', '0008_auto_20200104_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalconfigurations',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='socialmediasettings',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
