# Generated by Django 4.0.3 on 2022-05-09 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_box_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='box',
            name='phone',
            field=models.IntegerField(),
        ),
    ]
