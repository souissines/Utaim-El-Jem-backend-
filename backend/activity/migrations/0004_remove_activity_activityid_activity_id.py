# Generated by Django 4.0.3 on 2022-05-08 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0003_remove_activity_id_activity_activityid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='ActivityId',
        ),
        migrations.AddField(
            model_name='activity',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
