# Generated by Django 2.0.1 on 2018-05-25 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20180525_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='tag',
            field=models.CharField(default='', max_length=15, verbose_name='课程标签'),
        ),
    ]