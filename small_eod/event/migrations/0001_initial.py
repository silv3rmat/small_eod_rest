# Generated by Django 3.0.1 on 2020-01-03 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('case', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modifiedOn', models.DateTimeField(auto_now=True)),
                ('createdOn', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=256)),
                ('data', models.DateTimeField()),
                ('comment', models.CharField(max_length=256)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='case.Case')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
