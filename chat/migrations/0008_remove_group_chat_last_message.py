# Generated by Django 5.0.6 on 2024-06-12 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0007_group_chat_last_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group_chat',
            name='last_message',
        ),
    ]
