# Generated by Django 4.1.4 on 2022-12-17 14:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0003_alter_advert_brand_alter_advert_country_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='advert',
            name='addres',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
