# Generated by Django 4.1.4 on 2023-05-02 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cake', '0005_alter_orders_expected_deliverydate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cakes',
            name='layers',
            field=models.CharField(choices=[('one', 'one'), ('two', 'two'), ('three', 'three')], default='one', max_length=200),
        ),
        migrations.AlterField(
            model_name='cakes',
            name='shape',
            field=models.CharField(choices=[('circle', 'circle'), ('rectangle', 'rectangle'), ('oval', 'oval')], default='circle', max_length=300),
        ),
    ]