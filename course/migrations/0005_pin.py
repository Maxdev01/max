# Generated by Django 3.0.6 on 2020-08-02 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_auto_20200802_1124'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pin', models.CharField(max_length=6, unique=True)),
                ('used', models.BooleanField(default=False)),
            ],
        ),
    ]
