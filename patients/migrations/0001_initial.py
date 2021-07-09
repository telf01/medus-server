# Generated by Django 3.2.5 on 2021-07-09 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('lastname', models.CharField(max_length=60)),
                ('patronymic', models.CharField(max_length=60, null=True)),
                ('date_of_birth', models.DateField()),
                ('date_of_receipt', models.DateTimeField()),
                ('diagnosis', models.CharField(max_length=100, null=True)),
                ('appointment', models.TextField(max_length=10000, null=True)),
                ('comment', models.TextField(max_length=10000, null=True)),
            ],
        ),
    ]
