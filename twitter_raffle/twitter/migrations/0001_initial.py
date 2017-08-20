# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-18 21:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('created_at', models.DateTimeField()),
                ('favorite_count', models.IntegerField(default=0)),
                ('id_str', models.CharField(max_length=100, unique=True)),
                ('source', models.CharField(max_length=150)),
                ('text', models.CharField(max_length=150)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TwitterUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('description', models.CharField(max_length=300)),
                ('followers_count', models.IntegerField(default=0)),
                ('id_str', models.CharField(max_length=100, unique=True)),
                ('location', models.CharField(max_length=150)),
                ('name', models.CharField(max_length=30)),
                ('screen_name', models.CharField(max_length=60)),
                ('verified', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='tweet',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tweets', to='twitter.TwitterUser'),
        ),
    ]
