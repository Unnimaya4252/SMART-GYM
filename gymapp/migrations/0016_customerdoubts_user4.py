# Generated by Django 5.0.3 on 2024-04-22 06:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymapp', '0015_customercomplaint_user5'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerdoubts',
            name='user4',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]