# Generated by Django 3.2.3 on 2021-06-11 05:28

import custom_functions.models_functions
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import phonenumber_field.modelfields
import users.models.user_models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('locations', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('avatar', models.ImageField(default='user_avatar.jpg', upload_to=custom_functions.models_functions.upload_to)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, null=True, region=None)),
                ('nickname', models.CharField(default='User', max_length=100)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('age', models.CharField(blank=True, choices=[('F', 'All'), ('K', 'KID'), ('A', 'ADULT'), ('S', 'Senior')], max_length=1, null=True)),
                ('level', models.IntegerField(choices=[(1, 'NEW'), (2, 'REGULAR'), (3, 'ADVANCE'), (4, 'BUSINESS')], default=1)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='locations.location')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VerificationCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default=users.models.user_models.gen_code, max_length=6)),
                ('expire_time', models.DateTimeField(default=users.models.user_models.add_half_hour)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
