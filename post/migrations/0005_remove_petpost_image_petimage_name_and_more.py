# Generated by Django 4.1.7 on 2023-03-14 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_remove_petimage_name_petpost_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='petpost',
            name='image',
        ),
        migrations.AddField(
            model_name='petimage',
            name='name',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='post.petpost'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='petimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
