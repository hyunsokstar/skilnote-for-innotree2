# Generated by Django 3.2.11 on 2022-04-02 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts2', '0004_alter_profile_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='subject',
            field=models.CharField(blank=True, default='back', max_length=60, null=True),
        ),
    ]
