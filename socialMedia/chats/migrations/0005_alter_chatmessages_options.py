# Generated by Django 4.2.1 on 2023-06-05 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0004_alter_chatmessages_chat'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chatmessages',
            options={'ordering': ['-created_at'], 'verbose_name_plural': 'Chat Messages'},
        ),
    ]
