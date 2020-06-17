# Generated by Django 2.2.10 on 2020-06-11 13:33

import django.db.models.deletion
import django.db.models.manager
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0018_make_all_soft_deletable'),
    ]

    operations = [
        migrations.CreateModel(
            name='GovAgency',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True,
                                        serialize=False,
                                        verbose_name='ID')),
                ('agency_name', models.CharField(db_index=True,
                                                 max_length=20,
                                                 unique=True)),
                ('zip_code', models.DecimalField(decimal_places=0, max_digits=6)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RecycledFactory',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('api.factory',),
            managers=[
                ('recycle_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='RecycledImage',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('api.image',),
            managers=[
                ('recycle_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='RecycledReportRecord',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('api.reportrecord',),
            managers=[
                ('recycle_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True,
                                        serialize=False,
                                        verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('reason', models.TextField()),
                ('factory', models.ForeignKey(blank=True, null=True,
                                              on_delete=django.db.models.deletion.SET_NULL,
                                              related_name='reviews',
                                              to='api.Factory')),
                ('reviewer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                               related_name='reviews', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FollowUp',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('note', models.TextField(help_text='此次進度追蹤備註')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT,
                                               related_name='follow_ups', to='api.Factory')),
                ('staff', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                            related_name='follow_ups', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('code', models.CharField(help_text='公文號', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                              related_name='documents', to=settings.AUTH_USER_MODEL)),
                ('factory', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT,
                                              related_name='documents', to='api.Factory')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RecycledDocument',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('api.document',),
            managers=[
                ('recycle_objects', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='RecycledFollowUp',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('api.followup',),
            managers=[
                ('recycle_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]
