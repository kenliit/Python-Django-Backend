# Generated by Django 3.2.3 on 2021-06-20 02:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rating', '0005_auto_20210619_1758'),
        ('events', '0004_auto_20210617_1825'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='iov',
        ),
        migrations.CreateModel(
            name='EventIOV',
            fields=[
                ('imageorvideo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='rating.imageorvideo')),
                ('is_primary', models.BooleanField(default=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event')),
            ],
            options={
                'ordering': ('event', 'is_primary'),
            },
            bases=('rating.imageorvideo',),
        ),
    ]
