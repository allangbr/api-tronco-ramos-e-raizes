# Generated by Django 3.2.3 on 2021-06-04 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('midia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='tags',
            field=models.ManyToManyField(to='midia.Tag'),
        ),
    ]
