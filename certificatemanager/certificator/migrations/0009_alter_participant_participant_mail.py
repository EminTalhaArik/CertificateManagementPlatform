# Generated by Django 4.1.7 on 2023-03-14 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificator', '0008_alter_event_event_participants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='participant_mail',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]