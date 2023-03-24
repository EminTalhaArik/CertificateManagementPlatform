# Generated by Django 4.1.7 on 2023-03-24 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificator', '0009_alter_participant_participant_mail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('participant_name', models.CharField(max_length=100)),
                ('participant_mail', models.EmailField(max_length=254)),
                ('certificate_number', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='event',
            name='event_participants',
        ),
        migrations.DeleteModel(
            name='Participant',
        ),
        migrations.AddField(
            model_name='certificate',
            name='event',
            field=models.ManyToManyField(to='certificator.event'),
        ),
    ]
