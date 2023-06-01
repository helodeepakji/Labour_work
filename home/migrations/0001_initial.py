# Generated by Django 4.2.1 on 2023-06-01 13:38

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('username', models.CharField(max_length=20, unique=True)),
                ('Name', models.CharField(max_length=100)),
                ('Gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=10, null=True)),
                ('Is_worker', models.BooleanField(default=False)),
                ('Is_customer', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Education', models.CharField(blank=True, max_length=100, null=True)),
                ('Age', models.IntegerField()),
                ('Profile_pic', models.ImageField(blank=True, null=True, upload_to='profile_pic')),
                ('Category', models.CharField(max_length=100)),
                ('Gov_id_type', models.CharField(default='Aadhar', max_length=100)),
                ('Gov_id', models.CharField(blank=True, max_length=20, null=True)),
                ('Salary_type', models.CharField(choices=[('D_B', 'Daily Basis'), ('H_B', 'Hour Basis')], max_length=100)),
                ('Salary', models.IntegerField(blank=True, default=0, null=True)),
                ('Auth_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(max_length=100, unique=True)),
                ('Auth_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Area', models.CharField(max_length=100)),
                ('City', models.CharField(max_length=50)),
                ('State', models.CharField(max_length=50)),
                ('Pincode', models.CharField(max_length=10)),
                ('Default', models.BooleanField(default=False)),
                ('WorkerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.worker')),
            ],
        ),
    ]
