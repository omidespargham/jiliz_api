# Generated by Django 4.1.4 on 2022-12-17 14:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_city', models.CharField(max_length=80, verbose_name='name city')),
                ('state', models.CharField(max_length=80, verbose_name='state')),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=90)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='advert.category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('price', models.CharField(max_length=100)),
                ('agreement_price', models.BooleanField(default=False)),
                ('phone_number', models.CharField(max_length=12)),
                ('expired', models.BooleanField(default=True, verbose_name='وعضیت آگهی')),
                ('slug', models.SlugField(blank=True, editable=False, null=True, unique=True)),
                ('image0', models.ImageField(blank=True, default='defaults/default-thumbnail.jpg', null=True, upload_to='adverts_images/')),
                ('image1', models.ImageField(blank=True, default='defaults/default-thumbnail.jpg', null=True, upload_to='adverts_images/')),
                ('image2', models.ImageField(blank=True, default='defaults/default-thumbnail.jpg', null=True, upload_to='adverts_images/')),
                ('image3', models.ImageField(blank=True, default='defaults/default-thumbnail.jpg', null=True, upload_to='adverts_images/')),
                ('image4', models.ImageField(blank=True, default='defaults/default-thumbnail.jpg', null=True, upload_to='adverts_images/')),
                ('image5', models.ImageField(blank=True, default='defaults/default-thumbnail.jpg', null=True, upload_to='adverts_images/')),
                ('status_type', models.CharField(choices=[('new', 'نو'), ('worked', 'کارکرده')], max_length=30)),
                ('brand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='advert.brand')),
                ('category', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='advert.category')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advert.city')),
                ('country', models.ForeignKey(blank=True, default='IT', null=True, on_delete=django.db.models.deletion.CASCADE, to='advert.country')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
