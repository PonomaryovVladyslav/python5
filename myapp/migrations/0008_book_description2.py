# Generated by Django 5.0.3 on 2024-03-16 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_book_description1'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='description2',
            field=models.CharField(default='teetetetete', max_length=100),
            preserve_default=False,
        ),
    ]
