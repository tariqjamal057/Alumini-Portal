# Generated by Django 4.0.2 on 2022-05-10 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0005_alter_featured_sponser_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finance_request',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
