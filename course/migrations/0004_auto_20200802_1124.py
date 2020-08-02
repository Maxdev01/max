# Generated by Django 3.0.6 on 2020-08-02 18:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('course', '0003_auto_20200711_1118'),
    ]

    operations = [
        migrations.AddField(
            model_name='courses',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='courses',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
