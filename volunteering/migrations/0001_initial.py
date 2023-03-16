# Generated by Django 4.1.7 on 2023-03-15 17:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('post', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Volunteer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_confirm', models.BooleanField(default=False)),
                ('addres', models.TextField()),
                ('number', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('activation_code', models.UUIDField(default=uuid.uuid4)),
                ('animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pets', to='post.petpost')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pets', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
