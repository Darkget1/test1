# Generated by Django 4.2.3 on 2023-08-02 01:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_alter_project_setting_date_1st_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_setting',
            name='date_1st',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='project_setting',
            name='date_2nd',
            field=models.DateField(blank=True, default=django.utils.timezone.now),
        ),
    ]