# Generated by Django 5.0.4 on 2024-05-22 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_teacher_l_link_teacher_m_link_teacher_x_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(upload_to='media/course/'),
        ),
        migrations.AlterField(
            model_name='speciality',
            name='image',
            field=models.ImageField(upload_to='media/speciality/'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='image',
            field=models.ImageField(upload_to='media/teacher/'),
        ),
    ]
