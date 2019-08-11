# Generated by Django 2.1.4 on 2019-07-25 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mantra_site', '0004_auto_20190724_1738'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cover',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Section2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sec2_heading', models.CharField(max_length=255)),
                ('sec2_image1', models.ImageField(blank=True, null=True, upload_to='images')),
                ('sec2_image2', models.ImageField(blank=True, null=True, upload_to='images')),
            ],
        ),
    ]
