# Generated by Django 3.0.1 on 2020-01-03 17:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tagnamespace',
            name='createdBy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='tagnamespace_createdBy', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tagnamespace',
            name='modifiedBy',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='tagnamespace_modifiedBy', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tag',
            name='content_type',
            field=models.ForeignKey(limit_choices_to=models.Q(models.Q(('app_label', 'case'), ('model', 'Case')), models.Q(('app_label', 'api'), ('model', 'Letter')), _connector='OR'), on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
    ]