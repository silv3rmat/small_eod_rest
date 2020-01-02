# Generated by Django 3.0.1 on 2020-01-01 23:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_auto_20200101_2338'),
    ]

    operations = [
        migrations.CreateModel(
            name='Letter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modifiedOn', models.DateTimeField(auto_now=True)),
                ('createdOn', models.DateTimeField(auto_now_add=True)),
                ('direction', models.TextField(choices=[('IN', 'Received'), ('OUT', 'Sent')], default='IN', max_length=3)),
                ('createdBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='letter_createdBy', to=settings.AUTH_USER_MODEL)),
                ('modifiedBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='letter_modifiedBy', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]