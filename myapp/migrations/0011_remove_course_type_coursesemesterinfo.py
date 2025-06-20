# Generated by Django 5.1.4 on 2025-05-23 07:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_labroomused_start_time_alter_labroomused_lab_room'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='type',
        ),
        migrations.CreateModel(
            name='CourseSemesterInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('elective', 'elective'), ('supporting', 'supporting'), ('general', 'general'), ('major', 'major')], default='general', max_length=15)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.course')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.semester')),
            ],
            options={
                'unique_together': {('course', 'semester')},
            },
        ),
    ]
