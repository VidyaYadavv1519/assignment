# Generated by Django 4.2.2 on 2023-08-03 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=100)),
                ('package', models.FloatField()),
            ],
        ),
    ]
