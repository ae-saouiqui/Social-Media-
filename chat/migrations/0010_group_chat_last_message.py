# Generated by Django 5.0.6 on 2024-06-12 14:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0009_delete_message_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='group_chat',
            name='last_message',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='chat.message'),
        ),
    ]
