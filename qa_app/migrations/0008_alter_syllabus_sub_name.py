# Generated by Django 3.2.22 on 2024-05-07 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qa_app', '0007_qa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='syllabus',
            name='sub_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='qa_app.subject'),
        ),
    ]
