# Generated by Django 3.2.22 on 2024-05-06 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('qa_app', '0002_remove_subject_sub_bg'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject',
            old_name='sub_img',
            new_name='img',
        ),
    ]
