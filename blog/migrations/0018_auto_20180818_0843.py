# Generated by Django 2.0.7 on 2018-08-18 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20180818_0838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='rating',
            field=models.DecimalField(decimal_places=6, default=0.0, max_digits=7),
        ),
        migrations.AlterField(
            model_name='tag',
            name='rating',
            field=models.DecimalField(decimal_places=6, default=0.0, max_digits=7),
        ),
    ]