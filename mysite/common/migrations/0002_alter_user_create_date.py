# Generated by Django 4.2.3 on 2023-07-10 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='create_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='생성일'),
        ),
    ]
