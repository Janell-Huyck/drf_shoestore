# Generated by Django 3.0.7 on 2020-06-17 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoecolor',
            name='color_name',
            field=models.CharField(choices=[('R', 'Red'), ('O', 'Orange'), ('Y', 'Yellow'), ('G', 'Green'), ('B', 'Blue'), ('I', 'Indigo'), ('V', 'Violet'), ('WHITE', 'White'), ('BLACK', 'Black')], max_length=5),
        ),
    ]
