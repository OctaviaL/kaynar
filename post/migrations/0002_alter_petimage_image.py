# Generated by Django 4.1.7 on 2023-03-13 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='petimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
