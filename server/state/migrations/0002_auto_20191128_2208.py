# Generated by Django 2.2.7 on 2019-11-28 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('state', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='addition',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AlterField(
            model_name='state',
            name='answer',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='state',
            name='intent',
            field=models.CharField(max_length=32, null=True),
        ),
    ]