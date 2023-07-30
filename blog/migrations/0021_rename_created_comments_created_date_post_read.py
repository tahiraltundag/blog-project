# Generated by Django 4.2.3 on 2023-07-30 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_comments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='created',
            new_name='created_date',
        ),
        migrations.AddField(
            model_name='post',
            name='read',
            field=models.PositiveIntegerField(default=0),
        ),
    ]