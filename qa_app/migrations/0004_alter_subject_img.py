# Generated by Django 3.2.22 on 2024-05-07 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa_app', '0003_rename_sub_img_subject_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
