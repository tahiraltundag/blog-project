# Generated by Django 4.2.3 on 2023-07-29 07:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ForeignKey(default='software', on_delete=django.db.models.deletion.CASCADE, to='blog.category'),
        ),
    ]
