# Generated by Django 5.0.7 on 2024-07-17 13:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_student_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adhar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Adhar_no', models.IntegerField(unique=True)),
                ('Create_date', models.DateTimeField()),
                ('Create_by', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['Name'], 'verbose_name_plural': 'Student'},
        ),
        migrations.CreateModel(
            name='Brajesh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
                ('city', models.CharField(max_length=20)),
                ('Adhar_no', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.adhar')),
            ],
        ),
    ]
