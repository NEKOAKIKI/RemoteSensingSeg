# Generated by Django 4.1.4 on 2024-02-20 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='result_url',
            field=models.CharField(max_length=256, null=True, verbose_name='检测结果'),
        ),
    ]
