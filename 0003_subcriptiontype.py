# Generated by Django 2.2.5 on 2021-04-05 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_userinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubcriptionType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Subscriptiontypecode', models.CharField(max_length=20)),
                ('subscriptiontypename', models.CharField(max_length=20)),
            ],
        ),
    ]
