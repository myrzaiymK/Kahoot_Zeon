# Generated by Django 3.2 on 2022-08-04 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kahpril', '0005_alter_quiz_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='is_active',
        ),
        migrations.AlterField(
            model_name='quiz',
            name='player_passed',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='questions_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
