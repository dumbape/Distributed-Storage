# Generated by Django 2.1.7 on 2019-04-29 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0019_auto_20190427_2333'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeartBeatRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField()),
            ],
        ),
    ]
