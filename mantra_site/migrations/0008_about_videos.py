# Generated by Django 2.1.4 on 2019-07-31 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mantra_site', '0007_auto_20190725_2110'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='')),
                ('profile_para', models.TextField()),
                ('address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video1', models.URLField()),
                ('video1_heading', models.CharField(max_length=255)),
                ('video1_para', models.TextField()),
                ('video2', models.URLField()),
                ('video2_heading', models.CharField(max_length=255)),
                ('video2_para', models.TextField()),
                ('video3', models.URLField()),
                ('video3_heading', models.CharField(max_length=255)),
                ('video3_para', models.TextField()),
            ],
        ),
    ]
