# Generated by Django 3.2.13 on 2022-11-19 13:44

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=imagekit.models.fields.ProcessedImageField(blank=True, default='../static/images/profile/default.png', upload_to='profile/%Y%m%d/'),
        ),
    ]
