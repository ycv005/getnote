# Generated by Django 3.0.4 on 2020-03-28 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0003_auto_20200328_1623'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='note',
            options={'ordering': ['-last_modified']},
        ),
    ]