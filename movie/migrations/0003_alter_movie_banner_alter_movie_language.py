# Generated by Django 4.0 on 2021-12-31 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_alter_movie_banner_alter_movie_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='banner',
            field=models.FileField(upload_to='movies_banner'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='language',
            field=models.CharField(choices=[('english', 'ENGLISH'), ('german', 'GERMAN'), ('japan', 'JAPAN'), ('korea', 'KOREA'), ('china', 'CHINA')], max_length=10),
        ),
    ]