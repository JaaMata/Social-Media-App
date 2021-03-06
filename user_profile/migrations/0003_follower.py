# Generated by Django 3.2.8 on 2021-10-16 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_alter_post_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('follower_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followers', to='user_profile.profile')),
                ('following_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='following', to='user_profile.profile')),
            ],
        ),
    ]
