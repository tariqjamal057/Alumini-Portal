# Generated by Django 4.0 on 2022-02-26 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0005_authentication'),
    ]

    operations = [
        migrations.CreateModel(
            name='Corporsefund',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('total_amount', models.IntegerField()),
                ('modeofpayment', models.CharField(choices=[('O', 'Online Banking'), ('N', 'Net Banking'), ('U', 'UPI'), ('C', 'Credit/Debit card'), ('A', 'Cash')], max_length=1)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.user')),
            ],
        ),
        migrations.RemoveField(
            model_name='student_support',
            name='user',
        ),
        migrations.RenameField(
            model_name='authentication',
            old_name='is_active',
            new_name='isactive',
        ),
        migrations.DeleteModel(
            name='Sponser',
        ),
        migrations.DeleteModel(
            name='Student_Support',
        ),
    ]