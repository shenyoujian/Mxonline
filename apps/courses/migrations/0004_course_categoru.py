# Generated by Django 2.0.1 on 2018-05-25 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_course_course_org'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='categoru',
            field=models.CharField(default='', max_length=20, verbose_name='课程类别'),
        ),
    ]
