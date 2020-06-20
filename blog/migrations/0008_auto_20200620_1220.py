# Generated by Django 3.0.7 on 2020-06-20 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200619_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='parent',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='blog.Category', verbose_name='زیر دسته'),
        ),
        migrations.AlterField(
            model_name='category',
            name='position',
            field=models.IntegerField(default=0, verbose_name='پوزیشن'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True, verbose_name='ادرس دسته بندی'),
        ),
        migrations.AlterField(
            model_name='category',
            name='status',
            field=models.BooleanField(default=True, verbose_name='ایا نمایش داده شود؟'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=200, verbose_name='عنوان دسته'),
        ),
    ]