# Generated by Django 4.0.4 on 2022-05-29 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discription',
            field=models.CharField(default='', max_length=1000),
        ),
    ]
