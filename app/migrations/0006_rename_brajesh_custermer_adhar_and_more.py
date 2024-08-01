# Generated by Django 5.0.7 on 2024-07-19 11:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_school_studentmany'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Brajesh',
            new_name='Custermer_adhar',
        ),
        migrations.RemoveField(
            model_name='studentone',
            name='dep_name',
        ),
        migrations.CreateModel(
            name='Dpatment_job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('contect', models.IntegerField()),
                ('dep_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.department')),
            ],
        ),
        migrations.CreateModel(
            name='School_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('contect', models.IntegerField()),
                ('dep_name', models.ManyToManyField(to='app.school')),
            ],
        ),
        migrations.DeleteModel(
            name='Studentmany',
        ),
        migrations.DeleteModel(
            name='Studentone',
        ),
    ]