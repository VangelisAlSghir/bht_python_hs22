# Generated by Django 4.1.3 on 2023-01-16 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0005_alter_productreview_deleted_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productreview',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='productreview',
            name='reported',
            field=models.BooleanField(default=False),
        ),
    ]
