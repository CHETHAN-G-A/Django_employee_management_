# Generated by Django 4.1.1 on 2022-09-28 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0004_employee_hire_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='hire_date',
            field=models.DateField(),
        ),
    ]
