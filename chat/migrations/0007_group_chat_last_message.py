# Generated by Django 5.0.6 on 2024-06-12 14:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0006_remove_group_chat_last_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='group_chat',
            name='last_message',
            field=models.ForeignKey(default=12, on_delete=django.db.models.deletion.CASCADE, related_name='last_message', to='chat.message'),
            preserve_default=False,
        ),
    ]
