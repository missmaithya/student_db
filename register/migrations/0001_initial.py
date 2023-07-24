# Generated by Django 4.2.3 on 2023-07-24 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_no', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Full_name', models.CharField(max_length=30)),
                ('reg_no', models.CharField(default='', max_length=10)),
                ('email', models.EmailField(max_length=40)),
                ('contact', models.IntegerField(default=15)),
                ('registration', models.ForeignKey(default=10, on_delete=django.db.models.deletion.CASCADE, to='register.registration')),
            ],
        ),
    ]
