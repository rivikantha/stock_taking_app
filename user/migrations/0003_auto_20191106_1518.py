# Generated by Django 2.2.5 on 2019-11-06 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_user_group_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='group_no',
            field=models.IntegerField(null=True, verbose_name='group_no'),
        ),
    ]