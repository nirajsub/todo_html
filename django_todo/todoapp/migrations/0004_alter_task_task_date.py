# Generated by Django 3.2 on 2023-12-01 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0003_alter_task_task_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_date',
            field=models.DateField(),
        ),
    ]
