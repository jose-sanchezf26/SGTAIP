# Generated by Django 5.1.6 on 2025-03-06 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('session_id', models.CharField(max_length=100)),
                ('game_id', models.CharField(max_length=100)),
                ('event_type', models.CharField(max_length=100)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('data', models.JSONField()),
            ],
        ),
    ]
