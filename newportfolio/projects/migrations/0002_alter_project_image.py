# Generated by Django 4.2.16 on 2024-10-08 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='project_images/%Y/%m/%d/'),
        ),
    ]
