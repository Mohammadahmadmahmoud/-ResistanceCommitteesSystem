# Generated by Django 3.0.6 on 2020-06-08 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_project_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='Slug',
        ),
    ]
