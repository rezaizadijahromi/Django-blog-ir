# Generated by Django 3.0.7 on 2020-06-18 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200618_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('d', 'پیش نویش'), ('p', 'منتشر شدخ'), ('i', 'در حال بررسی'), ('b', 'برگشت داده شده')], max_length=1, verbose_name='وضعیت'),
        ),
    ]
