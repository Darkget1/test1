# Generated by Django 4.2.4 on 2023-08-04 05:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_project_setting_mall_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectUrl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mall_name', models.CharField(max_length=10)),
                ('url_title', models.CharField(blank=True, max_length=100, null=True)),
                ('url', models.TextField(blank=True, null=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.project')),
            ],
        ),
    ]
