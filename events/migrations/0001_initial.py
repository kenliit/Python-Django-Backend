# Generated by Django 3.2.3 on 2021-06-11 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdditionalInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condition', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Additional Info',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host', models.CharField(max_length=100)),
                ('theme', models.CharField(max_length=300)),
                ('description', models.TextField(max_length=1000)),
                ('event_type', models.CharField(choices=[('Live', 'Live'), ('Online', 'Online')], default='Live', max_length=10)),
                ('for_age', models.CharField(choices=[('F', 'All'), ('K', 'KID'), ('A', 'ADULT'), ('S', 'Senior')], default='A', max_length=1)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('open', models.TimeField()),
                ('close', models.TimeField()),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
