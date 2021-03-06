# Generated by Django 3.0.3 on 2020-02-16 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agg', '0002_auto_20200215_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='applied',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='job',
            name='hide',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='job',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
