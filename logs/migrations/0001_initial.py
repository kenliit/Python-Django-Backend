# Generated by Django 3.2.3 on 2021-06-11 05:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserLog',
            fields=[
                ('sessionId', models.AutoField(primary_key=True, serialize=False)),
                ('login_ip', models.GenericIPAddressField(blank=True, null=True)),
                ('login_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('country', models.CharField(blank=True, max_length=2, null=True)),
                ('region', models.CharField(blank=True, max_length=30, null=True)),
                ('city', models.CharField(blank=True, max_length=30, null=True)),
                ('isp', models.CharField(blank=True, max_length=50, null=True)),
                ('content', models.CharField(max_length=300)),
            ],
        ),
    ]
