# Generated by Django 5.1.3 on 2024-11-13 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_image_offrevoyage_main_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='offrevoyage',
            name='number_of_people',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]