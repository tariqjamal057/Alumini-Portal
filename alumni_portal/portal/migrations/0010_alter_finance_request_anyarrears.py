# Generated by Django 4.0.2 on 2022-03-09 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0009_alter_finance_request_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finance_request',
            name='anyarrears',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]