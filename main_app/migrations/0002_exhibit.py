# Generated by Django 5.1.4 on 2024-12-06 20:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exhibit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Exhibit date')),
                ('planet', models.CharField(choices=[('E', 'Earth'), ('M', 'Mars'), ('P', 'Pluto')], default='E', max_length=1)),
                ('artifact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.artifact')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
