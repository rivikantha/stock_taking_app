# Generated by Django 2.2.5 on 2019-11-10 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='database',
            name='author',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='author'),
        ),
        migrations.AddField(
            model_name='database',
            name='classification',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='classification'),
        ),
        migrations.AddField(
            model_name='database',
            name='loc',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='location code'),
        ),
        migrations.AddField(
            model_name='database',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='database',
            name='acc_no',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='accession number'),
        ),
        migrations.AlterField(
            model_name='database',
            name='pub_year',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='publication year'),
        ),
    ]
