# Generated by Django 2.2.7 on 2019-11-30 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('state', '0005_auto_20191130_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='answer',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
    ]