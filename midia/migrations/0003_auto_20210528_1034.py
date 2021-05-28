# Generated by Django 3.2.3 on 2021-05-28 13:34

from django.db import migrations, models
import midia.validators


class Migration(migrations.Migration):

    dependencies = [
        ('midia', '0002_auto_20210528_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='audio_album',
            field=models.FileField(upload_to=midia.validators.UploadToPath('images'), validators=[midia.validators.validate_file_size]),
        ),
        migrations.AlterField(
            model_name='document',
            name='file',
            field=models.FileField(upload_to=midia.validators.UploadToPath('images'), validators=[midia.validators.validate_file_size]),
        ),
    ]
