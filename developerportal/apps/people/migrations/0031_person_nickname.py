# Generated by Django 2.2.6 on 2019-10-08 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0030_add_social_image_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='nickname',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
