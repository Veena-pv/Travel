# Generated by Django 4.1.2 on 2022-10-18 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj2app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resort',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('img', models.ImageField(upload_to='pics')),
                ('details', models.TextField()),
            ],
        ),
    ]
