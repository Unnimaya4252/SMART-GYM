# Generated by Django 5.0.3 on 2024-05-01 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymapp', '0023_alter_idietadd_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerdoubts',
            name='reply',
            field=models.TextField(blank=True, null=True),
        ),
    ]
