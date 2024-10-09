# Generated by Django 5.1 on 2024-09-12 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateTimeField(verbose_name='Date of birth')),
                ('email', models.CharField(max_length=100)),
                ('app_date', models.DateTimeField(verbose_name='Date application was recieved')),
            ],
        ),
    ]
