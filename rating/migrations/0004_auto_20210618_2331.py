# Generated by Django 3.2.3 on 2021-06-19 05:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0003_remove_imageorvideo_is_primary'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='iov',
        ),
        migrations.AddField(
            model_name='comment',
            name='iov',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='rating.imageorvideo'),
        ),
        migrations.AlterField(
            model_name='imageorvideo',
            name='type',
            field=models.CharField(choices=[('YouTube', 'YOUTUBE'), ('Facebook', 'FACEBOOK'), ('Picture', 'PICTURE')], max_length=20),
        ),
        migrations.AlterField(
            model_name='imageorvideo',
            name='video_uri',
            field=models.CharField(blank=True, help_text='YouTube: only YouTube Id. Facebook: whole link', max_length=200, null=True),
        ),
    ]
