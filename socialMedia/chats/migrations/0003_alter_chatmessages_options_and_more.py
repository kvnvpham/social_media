# Generated by Django 4.2.1 on 2023-06-02 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chats', '0002_alter_chatmessages_options_alter_chats_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chatmessages',
            options={'verbose_name_plural': 'Chat Messages'},
        ),
        migrations.AlterField(
            model_name='chatmessages',
            name='content',
            field=models.TextField(max_length=150),
        ),
    ]
