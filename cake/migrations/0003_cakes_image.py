# Generated by Django 4.1.4 on 2023-04-28 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cake', '0002_alter_cakes_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='cakes',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]