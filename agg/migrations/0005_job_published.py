# Generated by Django 3.0.3 on 2020-02-16 13:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('agg', '0004_job_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='published',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
