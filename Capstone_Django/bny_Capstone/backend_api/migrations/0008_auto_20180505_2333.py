# Generated by Django 2.0 on 2018-05-05 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend_api', '0007_system_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='system',
            name='color',
            field=models.TextField(default='#a94442'),
        ),
    ]