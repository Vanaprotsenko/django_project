# Generated by Django 4.2.1 on 2023-07-08 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_post_text_of_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='text_of_comment',
        ),
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
