# Generated by Django 3.1.1 on 2020-10-07 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Your_locker', '0002_auto_20201008_0020'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500)),
                ('home_title', models.CharField(max_length=250)),
            ],
        ),
        migrations.DeleteModel(
            name='insider',
        ),
    ]