# Generated by Django 3.0 on 2020-01-08 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0002_person_p_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='timing',
        ),
        migrations.AddField(
            model_name='person',
            name='phone_no',
            field=models.CharField(default=9893550206, max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='person',
            name='p_name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='vehicle',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
