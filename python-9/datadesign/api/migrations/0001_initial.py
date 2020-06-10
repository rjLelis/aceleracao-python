# Generated by Django 3.0.6 on 2020-06-09 21:04

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('status', models.BooleanField()),
                ('env', models.CharField(max_length=20)),
                ('version', models.CharField(max_length=5)),
                ('address', models.GenericIPAddressField(protocol='IPV4')),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50, validators=[django.core.validators.MinValueValidator(8)])),
            ],
        ),
        migrations.CreateModel(
            name='GroupUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.Group')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.User')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.CharField(choices=[('CRITICAL', 'CRITICAL'), ('DEBUG', 'DEBUG'), ('ERROR', 'ERROR'), ('WARNING', 'WARNING'), ('INFO', 'INFO')], default='INFO', max_length=20)),
                ('data', models.TextField()),
                ('arquivado', models.BooleanField()),
                ('date', models.DateField(auto_now_add=True)),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Agent')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.User')),
            ],
        ),
        migrations.AddConstraint(
            model_name='event',
            constraint=models.CheckConstraint(check=models.Q(level__in=['CRITICAL', 'DEBUG', 'ERROR', 'WARNING', 'INFO']), name='api_event_level_valid'),
        ),
    ]
