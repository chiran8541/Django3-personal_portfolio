# Generated by Django 2.2 on 2020-06-27 21:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20200628_0218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='date',
        ),
        migrations.AddField(
            model_name='project',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='portfolio/images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
