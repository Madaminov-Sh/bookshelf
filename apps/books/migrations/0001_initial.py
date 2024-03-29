# Generated by Django 5.0.1 on 2024-02-20 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
                ('pages', models.IntegerField()),
                ('isbn', models.IntegerField(unique=True)),
                ('published', models.DateField()),
                ('started_time', models.DateField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
