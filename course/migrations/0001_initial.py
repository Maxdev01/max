# Generated by Django 3.0.6 on 2020-08-10 21:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField()),
                ('author', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('time', models.TimeField(blank=True, null=True)),
                ('url', models.CharField(blank=True, max_length=15, null=True)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Pin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pin', models.CharField(max_length=6, unique=True)),
                ('used', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ManyToManyField(blank=True, related_name='mescours', to='course.Courses')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='myuser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
