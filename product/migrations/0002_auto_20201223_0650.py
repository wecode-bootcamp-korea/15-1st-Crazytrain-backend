# Generated by Django 3.1.4 on 2020-12-23 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='optionsize',
            name='name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
