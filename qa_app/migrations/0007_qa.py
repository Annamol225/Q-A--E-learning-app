# Generated by Django 3.2.22 on 2024-05-07 13:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('qa_app', '0006_syllabus'),
    ]

    operations = [
        migrations.CreateModel(
            name='QA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qust', models.TextField()),
                ('ans', models.TextField()),
                ('sub_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qa_app.subject')),
                ('sy_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qa_app.syllabus')),
            ],
        ),
    ]
