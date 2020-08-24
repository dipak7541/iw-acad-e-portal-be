# Generated by Django 3.1 on 2020-08-13 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminsite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeacherRegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(upload_to='')),
                ('first_name', models.CharField(max_length=150)),
                ('middle_name', models.CharField(blank=True, max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('phone_no', models.CharField(max_length=10)),
                ('qualifications', models.TextField()),
                ('class_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminsite.addclassnumber')),
                ('subject_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminsite.addsubject')),
            ],
        ),
    ]