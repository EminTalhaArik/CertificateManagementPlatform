# Generated by Django 4.1.7 on 2023-03-24 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificator', '0013_rename_certificate_number_certificate_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='certificate_file',
            field=models.ImageField(null=True, upload_to='certificates'),
        ),
    ]