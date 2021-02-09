# Generated by Django 3.1.5 on 2021-02-08 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.PositiveIntegerField(default=0)),
                ('image', models.FilePathField(path='/Users/zoe/portfolio/react_ecommerce/public/images')),
            ],
        ),
    ]
