# Generated by Django 4.1.3 on 2022-11-29 13:56

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=1000)),
                ('fsk', models.IntegerField(choices=[(0, 'ab 0'), (6, 'ab 6'), (12, 'ab 12'), (16, 'ab 16'), (18, 'ab 18')])),
                ('price', models.FloatField()),
                ('image', models.FileField(upload_to='movies/images/')),
                ('pdf', models.FileField(upload_to='movies/pdf/')),
                ('creation_date', models.DateField(default=datetime.date.today)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', related_query_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=500)),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('deleted', models.BinaryField()),
                ('reported', models.BinaryField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Movies.movie')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'ProductReview',
                'verbose_name_plural': 'ProductReviews',
                'ordering': ['timestamp'],
            },
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('up_or_down', models.CharField(choices=[('U', 'up'), ('D', 'down')], max_length=1)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('productReview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Movies.productreview')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
