# Generated by Django 4.2.12 on 2024-07-31 17:43

import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0002_remove_customuser_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="username",
            field=models.CharField(
                default=django.utils.timezone.now,
                error_messages={"unique": "A user with that username already exists."},
                help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                max_length=150,
                unique=True,
                validators=[django.contrib.auth.validators.UnicodeUsernameValidator()],
                verbose_name="username",
            ),
            preserve_default=False,
        ),
    ]