# Generated by Django 5.2 on 2025-05-05 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_remove_course_lab_rooms_labroomused_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='labroomused',
            name='start_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='labroomused',
            name='lab_room',
            field=models.CharField(max_length=15),
        ),
    ]
