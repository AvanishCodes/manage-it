# Generated by Django 3.1.2 on 2020-11-19 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='partEvents',
            field=models.ManyToManyField(blank=True, related_name='participants', to='events.Event'),
        ),
    ]