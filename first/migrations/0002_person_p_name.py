# Generated by Django 3.0 on 2019-12-17 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='p_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
