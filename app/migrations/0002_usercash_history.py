# Generated by Django 4.2.6 on 2024-02-09 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCash_history',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=30)),
                ('amount', models.FloatField()),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('deposited_by_admin', models.CharField(max_length=30)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.studentdetails')),
            ],
        ),
    ]
