# Generated by Django 4.1.2 on 2022-11-15 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('second_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('tel_number', models.IntegerField()),
                ('location', models.CharField(max_length=20)),
                ('postal_code', models.IntegerField()),
                ('id_number', models.IntegerField()),
                ('gender', models.CharField(choices=[('male', 'MALE'), ('female', 'FEMALE'), ('other', 'OTHER')], default=None, max_length=6)),
                ('date_of_birth', models.DateTimeField(max_length=8)),
                ('date_of_register', models.DateTimeField(max_length=8)),
                ('email', models.EmailField(max_length=40)),
            ],
        ),
    ]
