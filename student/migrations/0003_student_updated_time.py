# Generated by Django 4.2.19 on 2025-03-05 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_student_created_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='updated_time',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='更新时间'),
        ),
    ]
