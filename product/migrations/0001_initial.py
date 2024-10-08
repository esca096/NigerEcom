# Generated by Django 5.1 on 2024-08-17 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=3, max_digits=100000)),
                ('image', models.ImageField(upload_to='')),
                ('slug', models.SlugField(null=True)),
                ('actif', models.BooleanField()),
            ],
        ),
    ]
