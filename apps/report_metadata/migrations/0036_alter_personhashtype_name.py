# Generated by Django 5.0.2 on 2024-03-19 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report_metadata', '0035_alter_personhashtype_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personhashtype',
            name='name',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]