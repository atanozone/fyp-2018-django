# Generated by Django 2.1.2 on 2018-10-11 14:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicSemester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startdate', models.DateTimeField(verbose_name='date start')),
                ('year', models.IntegerField(default=2000)),
                ('semester', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='EventDate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week_number', models.IntegerField(default=1)),
                ('day_number', models.IntegerField(default=1)),
                ('academicsemester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planner.AcademicSemester')),
            ],
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('EventDate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planner.EventDate')),
            ],
        ),
    ]