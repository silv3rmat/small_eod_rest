# Generated by Django 3.0.1 on 2020-01-02 02:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('collection', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectioncollectable',
            name='content_type',
            field=models.ForeignKey(limit_choices_to=models.Q(models.Q(('app_label', 'collection'), ('model', 'Event')), models.Q(('app_label', 'collection'), ('model', 'Note')), models.Q(('app_label', 'collection'), ('model', 'Letter')), _connector='OR'), on_delete=django.db.models.deletion.DO_NOTHING, to='contenttypes.ContentType'),
        ),
    ]