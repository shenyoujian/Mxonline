# Generated by Django 2.0.1 on 2018-05-29 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20180521_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='send_type',
            field=models.CharField(choices=[('register', '注册'), ('forget', '找回密码'), ('update_email', '修改邮箱')], max_length=10, verbose_name='发送类型'),
        ),
    ]
