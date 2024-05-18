# Generated by Django 4.2.11 on 2024-05-04 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_desc', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('task_name', models.CharField(max_length=200)),
            ],
        ),
    ]
