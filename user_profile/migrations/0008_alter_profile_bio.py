# Generated by Django 3.2.8 on 2021-11-03 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0007_alter_post_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
