# Generated by Django 2.2.5 on 2019-11-05 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crowdfunding', '0004_auto_20191105_1623'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adminer',
            fields=[
                ('admin_id', models.AutoField(primary_key=True, serialize=False)),
                ('admin_name', models.CharField(max_length=18)),
                ('admin_pwd', models.CharField(max_length=16)),
                ('admin_mobile', models.CharField(max_length=11)),
                ('admin_real_name', models.CharField(max_length=10, null=True)),
                ('admin_card', models.CharField(max_length=18, null=True)),
                ('admin_career', models.CharField(max_length=100, null=True)),
                ('admin_image', models.CharField(max_length=2000, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Admin',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_adress',
        ),
        migrations.AddField(
            model_name='user',
            name='user_address',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_image',
            field=models.CharField(max_length=2000, null=True),
        ),
    ]
