# Generated by Django 5.0.3 on 2024-05-18 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymapp', '0026_alter_membershipjoin_schedule_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=100)),
                ('fee_amount', models.IntegerField()),
            ],
        ),
    ]
