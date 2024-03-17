# Generated by Django 5.0.3 on 2024-03-16 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_author_book'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['headline']},
        ),
        migrations.RenameField(
            model_name='article',
            old_name='name',
            new_name='headline',
        ),
        migrations.RemoveField(
            model_name='article',
            name='text',
        ),
        migrations.AddField(
            model_name='article',
            name='publications',
            field=models.ManyToManyField(to='myapp.publication'),
        ),
    ]
