# Generated by Django 4.1.7 on 2023-03-16 05:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PetPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('male', 'мальчик'), ('female', 'девочка')], max_length=10)),
                ('description', models.TextField()),
                ('category', models.CharField(choices=[('dogs', 'собаки'), ('cats', 'кошки')], max_length=20)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='petposts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PetImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='post.petpost')),
            ],
        ),
    ]
