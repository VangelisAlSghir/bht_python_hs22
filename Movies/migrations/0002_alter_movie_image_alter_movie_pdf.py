# Generated by Django 4.1.3 on 2022-12-07 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image',
            field=models.FileField(blank=True, upload_to='movies/images/'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='pdf',
            field=models.FileField(blank=True, upload_to='movies/pdf/'),
        ),
    ]
