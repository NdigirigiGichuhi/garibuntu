# Generated by Django 4.2.16 on 2024-10-31 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_eventregistration_payment_confirmation_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='poster',
            field=models.ImageField(blank=True, null=True, upload_to='event_posters/'),
        ),
    ]