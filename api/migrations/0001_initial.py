# Generated by Django 5.1.7 on 2025-04-27 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ename', models.CharField(max_length=60)),
                ('esal', models.FloatField()),
                ('eaddr', models.CharField(max_length=60)),
                ('designation', models.CharField(max_length=255)),
            ],
        ),
    ]
