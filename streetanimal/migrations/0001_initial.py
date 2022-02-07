# Generated by Django 3.2.12 on 2022-02-07 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('animal_no', models.AutoField(primary_key=True, serialize=False)),
                ('size', models.CharField(max_length=30)),
                ('sex', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('date_of_discovery', models.DateTimeField()),
                ('place_of_discovery', models.DateTimeField()),
                ('physical_condition', models.CharField(max_length=200)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('protection_status', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
