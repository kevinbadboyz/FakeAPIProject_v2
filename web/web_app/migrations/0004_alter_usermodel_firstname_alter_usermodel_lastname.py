# Generated by Django 5.1.4 on 2024-12-05 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_app', '0003_alter_game_name_alter_game_user_create_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='firstName',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='lastName',
            field=models.CharField(max_length=100),
        ),
    ]
