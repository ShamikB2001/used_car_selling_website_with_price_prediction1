# Generated by Django 3.2.7 on 2022-05-04 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('carsale', '0003_auto_20220504_1228'),
    ]

    operations = [
        migrations.CreateModel(
            name='create_acc_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aname', models.CharField(max_length=200)),
                ('aemail', models.CharField(max_length=200)),
                ('aphoneno', models.CharField(max_length=20)),
                ('apassword', models.CharField(max_length=200)),
                ('acpassword', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'create_acc_details',
            },
        ),
    ]
