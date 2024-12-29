# Generated by Django 4.2.16 on 2024-11-19 16:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0013_alter_enquiry_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='user',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='enquiries', to=settings.AUTH_USER_MODEL),
        ),
    ]
