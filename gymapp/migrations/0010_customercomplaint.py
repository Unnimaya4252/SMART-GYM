# Generated by Django 5.0.3 on 2024-03-30 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymapp', '0009_remove_customerdoubts_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerComplaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('complaints', models.TextField()),
            ],
        ),
    ]