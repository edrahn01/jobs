# Generated by Django 3.0.3 on 2020-02-16 13:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('agg', '0003_auto_20200215_2313'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='link',
            field=models.CharField(default=django.utils.timezone.now, max_length=300),
            preserve_default=False,
        ),
    ]
