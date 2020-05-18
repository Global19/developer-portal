# Generated by Django 2.2.12 on 2020-05-07 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mozimages', '0001_initial'),
        ('videos', '0012_remove_video_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='card_image_3_2',
            field=models.ForeignKey(blank=True, help_text='An image in 3:2 aspect ratio', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='mozimages.MozImage', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='video',
            name='card_image',
            field=models.ForeignKey(blank=True, help_text='An image in 16:9 aspect ratio', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='mozimages.MozImage', verbose_name='Image'),
        ),
    ]
