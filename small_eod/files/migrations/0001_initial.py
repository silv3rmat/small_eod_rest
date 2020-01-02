# Generated by Django 3.0.1 on 2020-01-02 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.FilePathField()),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FileSigner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('method', models.CharField(choices=[('POST', 'POST'), ('PUT', 'PUT')], default='POST', max_length=4)),
                ('url', models.URLField()),
                ('path', models.FilePathField()),
            ],
        ),
    ]