# Generated by Django 2.2.5 on 2019-10-29 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crowdfunding', '0002_fundraiser_projects'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Fundraiser',
            new_name='Fundraisers',
        ),
        migrations.RenameModel(
            old_name='Projects',
            new_name='Project',
        ),
    ]
