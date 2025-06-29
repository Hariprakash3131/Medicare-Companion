# Generated by Django 5.2.3 on 2025-06-25 17:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_medicationrecord'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicationrecord',
            name='proof_photo',
            field=models.ImageField(blank=True, null=True, upload_to='proof_photos/'),
        ),
        migrations.AlterUniqueTogether(
            name='medicationrecord',
            unique_together={('user', 'date')},
        ),
    ]
