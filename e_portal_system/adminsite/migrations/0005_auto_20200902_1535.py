# Generated by Django 3.1 on 2020-09-02 15:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminsite', '0004_auto_20200902_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticeupload',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username'),
        ),
    ]