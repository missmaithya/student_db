# Generated by Django 4.2.3 on 2023-07-24 09:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='hostel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostel_name', models.CharField(max_length=100)),
                ('room_type', models.CharField(choices=[('dormitory', 'Dormitory'), ('private', 'Private Room')], max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('rating', models.DecimalField(decimal_places=2, max_digits=3)),
                ('availability', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='hostel_allocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in_date', models.DateField()),
                ('check_out_date', models.DateField()),
                ('hostel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.hostel')),
                ('student_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='register.student')),
            ],
        ),
    ]
