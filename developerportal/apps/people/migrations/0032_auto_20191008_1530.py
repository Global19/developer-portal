# Generated by Django 2.2.6 on 2019-10-08 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0031_person_nickname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='role',
            field=models.CharField(choices=[('staff', 'Staff'), ('tech-speaker', 'Tech Speaker'), ('community', 'Community')], default='staff', max_length=250),
        ),
    ]
