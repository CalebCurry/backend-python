# Generated by Django 4.0.3 on 2022-04-09 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('files', '0004_alter_file_upload_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='upload_timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]