# Generated by Django 2.2.5 on 2020-06-28 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vente_parcelle', '0003_document_buyer_commune'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='buyer_commune',
        ),
    ]