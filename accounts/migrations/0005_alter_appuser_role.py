# Generated by Django 4.2.1 on 2023-05-30 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_appuser_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='role',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Client', 'Client')], default='Client', max_length=15),
        ),
    ]
