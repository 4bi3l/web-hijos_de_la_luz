# Generated by Django 2.0.2 on 2019-06-07 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(default='gallery/static/images/no-img.jpg', upload_to='gallery'),
        ),
    ]
