# Generated by Django 3.0.7 on 2022-10-20 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0006_auto_20221020_1147'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentresult',
            name='subject_total',
            field=models.FloatField(default=0, null=True),
        ),
    ]
