# Generated by Django 3.0.7 on 2020-06-19 05:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20200618_2227'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('position',), 'verbose_name': 'دسته بندی', 'verbose_name_plural': 'دستع بندی ها'},
        ),
    ]
