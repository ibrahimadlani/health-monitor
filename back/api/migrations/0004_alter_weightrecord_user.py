# Generated by Django 5.0.9 on 2024-09-10 15:42

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_alter_weightrecord_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="weightrecord",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
