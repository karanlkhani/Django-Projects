# Generated by Django 4.2.3 on 2024-04-17 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Calculator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('principal_amount', models.FloatField()),
                ('interest_rate', models.FloatField()),
                ('time_period', models.FloatField()),
            ],
        ),
    ]
