# Generated by Django 2.1.2 on 2020-06-11 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='sample_1',
        ),
        migrations.RemoveField(
            model_name='item',
            name='sample_10',
        ),
        migrations.RemoveField(
            model_name='item',
            name='sample_2',
        ),
        migrations.RemoveField(
            model_name='item',
            name='sample_3',
        ),
        migrations.RemoveField(
            model_name='item',
            name='sample_4',
        ),
        migrations.RemoveField(
            model_name='item',
            name='sample_5',
        ),
        migrations.RemoveField(
            model_name='item',
            name='sample_6',
        ),
        migrations.RemoveField(
            model_name='item',
            name='sample_7',
        ),
        migrations.RemoveField(
            model_name='item',
            name='sample_8',
        ),
        migrations.RemoveField(
            model_name='item',
            name='sample_9',
        ),
        migrations.AddField(
            model_name='item',
            name='author',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='著者'),
        ),
        migrations.AddField(
            model_name='item',
            name='buydate',
            field=models.DateField(blank=True, null=True, verbose_name='購入日 日付'),
        ),
        migrations.AddField(
            model_name='item',
            name='memo',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='メモ、感想'),
        ),
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='価格'),
        ),
        migrations.AddField(
            model_name='item',
            name='publisher',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='出版社'),
        ),
        migrations.AddField(
            model_name='item',
            name='recommended',
            field=models.IntegerField(blank=True, null=True, verbose_name='オヌヌメ度'),
        ),
        migrations.AddField(
            model_name='item',
            name='title',
            field=models.CharField(blank=True, max_length=300, null=True, verbose_name='タイトル'),
        ),
    ]
