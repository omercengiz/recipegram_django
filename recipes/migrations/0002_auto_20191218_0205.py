# Generated by Django 2.1.5 on 2019-12-17 23:05

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='recipe_image',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Please,Add an image...'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='content',
            field=ckeditor.fields.RichTextField(),
        ),
    ]