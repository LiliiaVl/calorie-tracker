# Generated by Django 4.2.2 on 2023-06-30 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='calories',
            field=models.IntegerField(),
        ),
    ]