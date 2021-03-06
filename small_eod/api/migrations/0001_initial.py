# Generated by Django 3.0.1 on 2020-01-03 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_field', models.CharField(max_length=256)),
                ('object_id', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TagNamespace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modifiedOn', models.DateTimeField(auto_now=True)),
                ('createdOn', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(max_length=256)),
                ('color', models.CharField(default='0000000000', max_length=9)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
