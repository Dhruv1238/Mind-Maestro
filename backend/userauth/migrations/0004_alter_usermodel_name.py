# Generated by Django 5.0.1 on 2024-01-21 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauth', '0003_usermodel_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
