# Generated by Django 4.0.2 on 2022-05-10 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0006_alter_finance_request_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finance_request',
            name='image',
            field=models.ImageField(upload_to='student_images'),
        ),
    ]
