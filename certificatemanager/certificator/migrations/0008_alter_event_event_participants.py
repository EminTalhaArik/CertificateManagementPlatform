# Generated by Django 4.1.7 on 2023-03-12 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificator', '0007_event_event_participants_alter_eventtype_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_participants',
            field=models.ManyToManyField(to='certificator.participant'),
        ),
    ]
