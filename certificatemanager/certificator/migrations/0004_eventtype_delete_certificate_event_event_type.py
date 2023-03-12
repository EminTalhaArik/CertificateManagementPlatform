# Generated by Django 4.1.7 on 2023-03-12 12:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('certificator', '0003_alter_event_event_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Certificate',
        ),
        migrations.AddField(
            model_name='event',
            name='event_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='certificator.eventtype'),
        ),
    ]
