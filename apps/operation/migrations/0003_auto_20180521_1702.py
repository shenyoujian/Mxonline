# Generated by Django 2.0.1 on 2018-05-21 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0002_userfavorite_add_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfavorite',
            name='fav_id',
            field=models.IntegerField(default=0, verbose_name='收藏id'),
        ),
    ]