# Generated by Django 3.0.6 on 2020-07-01 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20200625_1755'),
    ]

    operations = [
        migrations.CreateModel(
            name='FamilyMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=150)),
                ('Age', models.PositiveIntegerField()),
                ('Gender', models.CharField(choices=[('ML', 'male'), ('FM', 'female')], default='ML', max_length=2)),
                ('Relative_Relation', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='family',
            name='Date_Of_Birth',
        ),
        migrations.AddField(
            model_name='family',
            name='Age',
            field=models.PositiveIntegerField(default=None),
            preserve_default=False,
        ),
    ]
