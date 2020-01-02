# Generated by Django 3.0.1 on 2020-01-01 23:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddressData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('voivodeship', models.CharField(max_length=100)),
                ('flat_no', models.CharField(blank=True, max_length=100, null=True)),
                ('street', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=100)),
                ('house_no', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('epuap', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AdministrativeUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
                ('terc', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('level', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ExternalIdentifier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nip', models.CharField(max_length=100)),
                ('regon', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('createdOn', models.DateTimeField(auto_now_add=True)),
                ('modifiedOn', models.DateTimeField(auto_now=True)),
                ('address', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='institution.AddressData')),
                ('administrativeUnit', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='institution.AdministrativeUnit')),
            ],
        ),
    ]