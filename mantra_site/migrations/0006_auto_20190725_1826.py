# Generated by Django 2.1.4 on 2019-07-25 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mantra_site', '0005_cover_section2'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tiles',
            options={},
        ),
        migrations.AlterField(
            model_name='tiles',
            name='heading',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
