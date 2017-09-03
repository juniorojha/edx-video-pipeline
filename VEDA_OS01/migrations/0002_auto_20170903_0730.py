# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-03 07:30
from __future__ import unicode_literals

import VEDA_OS01.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('VEDA_OS01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TranscriptCredentials',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('org', models.CharField(help_text=b'This value must match the value of organization in studio/edx-platform.', max_length=50, verbose_name=b'Organization')),
                ('provider', models.CharField(choices=[(b'3PlayMedia', b'3PlayMedia'), (b'Cielo24', b'Cielo24')], max_length=50, verbose_name=b'Transcript provider')),
                ('api_key', models.CharField(max_length=255, verbose_name=b'API key')),
                ('api_secret', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'API secret')),
            ],
            options={
                'verbose_name_plural': 'Transcript Credentials',
            },
        ),
        migrations.CreateModel(
            name='TranscriptProcessMetadata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('provider', models.CharField(choices=[(b'3PlayMedia', b'3PlayMedia'), (b'Cielo24', b'Cielo24')], max_length=50, verbose_name=b'Transcript provider')),
                ('process_id', models.CharField(max_length=255, verbose_name=b'Process id')),
                ('translation_id', models.CharField(blank=True, max_length=255, null=True, verbose_name=b'Translation id')),
                ('lang_code', models.CharField(max_length=8, verbose_name=b'Language code')),
                ('status', models.CharField(choices=[(b'PENDING', b'PENDING'), (b'IN PROGRESS', b'IN PROGRESS'), (b'FAILED', b'FAILED'), (b'READY', b'READY')], default=b'PENDING', max_length=50, verbose_name=b'Transcript status')),
            ],
            options={
                'get_latest_by': 'modified',
                'verbose_name_plural': 'Transcript process metadata',
            },
        ),
        migrations.AddField(
            model_name='video',
            name='cielo24_fidelity',
            field=models.CharField(blank=True, choices=[(b'MECHANICAL', b'Mechanical, 75% Accuracy'), (b'PREMIUM', b'Premium, 95% Accuracy'), (b'PROFESSIONAL', b'Professional, 99% Accuracy')], max_length=20, null=True, verbose_name=b'Cielo24 Fidelity'),
        ),
        migrations.AddField(
            model_name='video',
            name='cielo24_turnaround',
            field=models.CharField(blank=True, choices=[(b'STANDARD', b'Standard, 48h'), (b'PRIORITY', b'Priority, 24h')], max_length=20, null=True, verbose_name=b'Cielo24 Turnaround'),
        ),
        migrations.AddField(
            model_name='video',
            name='preferred_languages',
            field=VEDA_OS01.models.ListField(blank=True, default=[]),
        ),
        migrations.AddField(
            model_name='video',
            name='process_transcription',
            field=models.BooleanField(default=False, verbose_name=b'Process transcripts from Cielo24/3PlayMedia'),
        ),
        migrations.AddField(
            model_name='video',
            name='provider',
            field=models.CharField(blank=True, choices=[(b'3PlayMedia', b'3PlayMedia'), (b'Cielo24', b'Cielo24')], max_length=20, null=True, verbose_name=b'Transcription provider'),
        ),
        migrations.AddField(
            model_name='video',
            name='three_play_turnaround',
            field=models.CharField(blank=True, choices=[(b'extended_service', b'10-Day/Extended'), (b'default', b'4-Day/Default'), (b'expedited_service', b'2-Day/Expedited'), (b'rush_service', b'24 hour/Rush'), (b'same_day_service', b'Same Day')], max_length=20, null=True, verbose_name=b'3PlayMedia Turnaround'),
        ),
        migrations.AlterField(
            model_name='video',
            name='video_trans_status',
            field=models.CharField(choices=[(b'Ingest', b'System Ingest'), (b'Transcode Queue', b'Transcode Queue'), (b'Active Transcode', b'Active Transcode'), (b'Transcode Retry', b'Transcode Retry'), (b'Transcode Complete', b'Transcode Complete'), (b'Deliverable Upload', b'Deliverable Upload'), (b'File Complete', b'File Complete'), (b'Transcode Error', b'Transcode Error'), (b'Corrupt File', b'Corrupt File on Ingest'), (b'Review Hold', b'Review Hold'), (b'Review Reject', b'Review Rejected'), (b'Final Publish', b'Review to Final Publish'), (b'Youtube Duplicate', b'Youtube Duplicate'), (b'In Encode Queue', b'In Encode Queue'), (b'Progress', b'In Progress'), (b'Complete', b'Complete'), (b'transcription_in_progress', b'Transcription In Progress'), (b'transcription_ready', b'Transcription Ready')], default=b'Ingest', max_length=100, verbose_name=b'Transcode Status'),
        ),
        migrations.AddField(
            model_name='transcriptprocessmetadata',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VEDA_OS01.Video'),
        ),
        migrations.AlterUniqueTogether(
            name='transcriptcredentials',
            unique_together=set([('org', 'provider')]),
        ),
    ]
