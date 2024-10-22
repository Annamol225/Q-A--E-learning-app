# Generated by Django 3.2.22 on 2024-05-13 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qa_app', '0013_alter_syllabus_sub_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qa',
            name='sy_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qust', to='qa_app.syllabus'),
        ),
        migrations.AlterField(
            model_name='syllabus',
            name='sub_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sy_list', to='qa_app.subject'),
        ),
    ]
