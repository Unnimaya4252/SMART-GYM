# Generated by Django 5.0.3 on 2024-04-16 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gymapp', '0013_customerfee'),
    ]

    operations = [
        migrations.CreateModel(
            name='DietInst',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breakfast', models.TextField()),
                ('lunch', models.TextField()),
                ('dinner', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='CustomerComplaintAdmin',
        ),
        migrations.DeleteModel(
            name='Diet',
        ),
        migrations.AddField(
            model_name='customercomplaint',
            name='reply',
            field=models.TextField(blank=True, null=True),
        ),
    ]
