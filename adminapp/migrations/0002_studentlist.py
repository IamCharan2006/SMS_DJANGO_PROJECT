# Generated by Django 5.0.7 on 2024-09-18 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Register_Number', models.CharField(max_length=20, unique=True)),
                ('Name', models.CharField(max_length=100)),
            ],
        ),
    ]
