# Generated by Django 2.2.5 on 2021-04-05 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_subcriptiontype'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Servicecode', models.CharField(max_length=20)),
                ('servicename', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=20)),
                ('premium', models.CharField(max_length=20)),
                ('allocation', models.CharField(max_length=20)),
            ],
        ),
    ]
